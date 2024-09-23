import streamlit as st
from design.styles import load_global_styles, load_welcome_page_styles, load_explanation_page_styles, load_recommendations_page_styles, load_button_styles
from model.preprocess import preprocess_data
from model.knn import get_knn_recommendations, get_recommendations_by_favorite_games

load_global_styles()

if 'proceed_choice' not in st.session_state:
    st.session_state.proceed_choice = None
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def show_welcome_page():
    load_welcome_page_styles()

    if st.button("Let's go"):
        st.session_state.page = 'explanation'
        st.rerun()

def show_explanation_page():
    load_explanation_page_styles()
    if st.button("Absolutely!"):
        st.session_state.page = 'recommendations'
        st.rerun()

def show_recommendations():
    if 'proceed_choice' not in st.session_state:
        st.session_state.proceed_choice = None

    df, unique_mechanics, unique_themes = preprocess_data('bgg_db_1806.csv')
    load_recommendations_page_styles()
    audio_file = open('hail-126903.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', start_time=0)

    st.markdown('<div class="custom-input-label">The ritual begins. Answer my questions truthfully, and the magic shall unfold. Is there already a game that stirs your soul, favorite among your collection?</div>', unsafe_allow_html=True)
    
    load_button_styles() 

    col1, col2 = st.columns(2)
    with col1:
        if st.button("I remembered some from last time."):
            st.session_state.proceed_choice = 'remembered'
    with col2:
            if st.button("No, this is why I'm here!"):
             st.session_state.proceed_choice = 'no_favorite'
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.proceed_choice is None:
        return
    
    if st.session_state.proceed_choice == 'remembered':
        # Step 1: Favorite game input
        st.markdown('<div class="custom-input-label"> A wondrous inclination! The magic bubble awaits your chosen game. Speak its name by typing it here below. </div>', unsafe_allow_html=True)
        favorite_game = st.text_input(' ')  # Empty label for the input field
        selected_game = None
        favorite_games = [favorite_game] if favorite_game else []

        if favorite_game:
            filtered_games = df[df['names'].str.contains(favorite_game, case=False, na=False)]
            if filtered_games.empty:
                st.markdown('<div class="custom-input-label">No game found.. Please choose a game from this deck:</div>', unsafe_allow_html=True)
                all_games = df['names'].dropna().unique()
                selected_game = st.selectbox('', all_games, key='selectbox_all_games')
            else:
                st.markdown('<div class="custom-input-label">Marvelous! These games are like magical creatures, each with its own special charm. Choose one.</div>', unsafe_allow_html=True)
                game_options = filtered_games['names'].dropna().unique()
                selected_game = st.selectbox('', game_options, key='selectbox_filtered_games')
    
        st.markdown('<div class="custom-input-label">Shall we add more games to our magical brew?</div>', unsafe_allow_html=True)
        more_games = st.radio("", ("No", "Yes"), key="more_games_radio")
        additional_games = []

        if more_games == "Yes":
            for i in range(2):
                st.markdown(f'<div class="custom-input-label">Think of a {i+2}. game:</div>', unsafe_allow_html=True)
                additional_game = st.text_input(' ', key=f'ingredient_{i}')

                if additional_game:
                    filtered_games = df[df['names'].str.contains(additional_game, case=False, na=False)]
                    if filtered_games.empty:
                        st.markdown('<div class="custom-input-label">Oh no. Evil spirits. Please choose a different game</div>', unsafe_allow_html=True)
                        all_games = df['names'].dropna().unique()
                        selected_game = st.selectbox('', all_games, key=f'selectbox_all_games_{i}')
                    else:
                        st.markdown('<div class="custom-input-label">Do these games align with your desires?</div>', unsafe_allow_html=True)
                        game_options = filtered_games['names'].dropna().unique()
                        selected_game = st.selectbox('', game_options, key=f'selectbox_filtered_games_{i}')
                    favorite_games.append(selected_game)
                additional_games.append(additional_game)

        st.markdown('<div class="custom-input-label">Are you prepared for more questions to delve deeper?</div>', unsafe_allow_html=True)
        more_questions = st.radio("", ("No", "Yes"), key="more_questions_radio")

        show_recommendations_button = False

        if more_questions == "Yes":
            st.markdown('<div class="custom-input-label">A delightful preference! With how many companions do you prefer to play an adventure?</div>', unsafe_allow_html=True)
            num_players = st.selectbox('', sorted(df['min_players'].dropna().unique()), key='num_players')

            st.markdown('<div class="custom-input-label">And for how many minutes shall your game endure?</div>', unsafe_allow_html=True)
            game_duration = st.selectbox('', ['0-30', '30-60', '60-120', '120+'], key='game_duration')

            st.markdown('<div class="custom-input-label">What hidden essence shall we stir into our potion?</div>', unsafe_allow_html=True)
            game_theme = st.selectbox('', unique_themes, key='game_theme')

            st.markdown('<div class="custom-input-label">A fine choice! Which level of difficulty do you desire? 1 is for beginner, 2 is normal, 3 is medium, 4 is difficult and 5 is only for board game elites.</div>', unsafe_allow_html=True)
            game_difficulty = st.selectbox('', sorted(df['weight'].dropna().unique()), key='game_difficulty')

            st.markdown('<div class="custom-input-label">Near the end of our spell... What minimum age should your game be suitable for?</div>', unsafe_allow_html=True)
            game_age = st.selectbox('', sorted(df['age'].dropna().unique()), key='game_age')

            
            if st.button("Show me my prediction pot!"):
                recommended_games = get_knn_recommendations(df, num_players, game_duration, game_theme, game_difficulty, game_age)
                recommended_games['bgg_url'] = recommended_games['bgg_url'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
                st.markdown('<div class="custom-input-label">Behold! The fruits of our divination. These games are tailored to your desires, my dear!</div>', unsafe_allow_html=True)
                st.write(" ")
                st.markdown("<div class='styled-table'>" + recommended_games.rename(columns={'names': 'Title', 'bgg_url': 'Link to the description'}).to_html(classes='styled-table', escape=False, index=False) + "</div>", unsafe_allow_html=True)
                show_recommendations_button = True

       
        if more_questions == "No":
            if st.button("Show me my prediction pot based on my favorite board games!"):
                missing_games = [i+2 for i, game in enumerate(additional_games) if not game] 
                if not favorite_game:  
                    st.markdown('<div class="warning-text">Don\'t forget to use the magic bubble to enter your 1. game!</div>', unsafe_allow_html=True)
                elif missing_games:
                    for i in missing_games:
                        st.markdown(f'<div class="warning-text">Don\'t forget to use the magic bubbles to enter your {i}. game!</div>', unsafe_allow_html=True)
                else:
                    if favorite_games:
                        recommended_games = get_recommendations_by_favorite_games(df, favorite_games)
                        if recommended_games.empty:
                            st.write("No games found that suited your game description.")
                        else:
                            recommended_games['bgg_url'] = recommended_games['bgg_url'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
                            st.markdown("<div class='styled-table'>" + recommended_games.rename(columns={'names': 'Title', 'bgg_url': 'Link to the description'}).to_html(classes='styled-table', escape=False, index=False) + "</div>", unsafe_allow_html=True)
                            show_recommendations_button = True

        if show_recommendations_button:
            if st.button("Again!"):
                st.session_state.page = 'recommendations'
                st.rerun()


    elif st.session_state.proceed_choice == 'no_favorite':   
        st.markdown('<div class="custom-input-label">A delightful preference! With how many companions do you prefer to play an adventure?</div>', unsafe_allow_html=True)
        num_players = st.selectbox('', sorted(df['min_players'].dropna().unique()), key='num_players')

        st.markdown('<div class="custom-input-label">And for how many minutes shall your game endure?</div>', unsafe_allow_html=True)
        game_duration = st.selectbox('', ['0-30', '30-60', '60-120', '120+'], key='game_duration')

        st.markdown('<div class="custom-input-label">What hidden essence shall we stir into our potion?</div>', unsafe_allow_html=True)
        game_theme = st.selectbox('', unique_themes, key='game_theme')

        st.markdown('<div class="custom-input-label">A fine choice! Which level of difficulty do you desire? 1 is for beginner, 2 is normal, 3 is medium, 4 is difficult and 5 is only for board game elites.</div>', unsafe_allow_html=True)
        game_difficulty = st.selectbox('', sorted(df['weight'].dropna().unique()), key='game_difficulty')

        st.markdown('<div class="custom-input-label">Near the end of our spell... What minimum age should your game be suitable for?</div>', unsafe_allow_html=True)
        game_age = st.selectbox('', sorted(df['age'].dropna().unique()), key='game_age')

        if st.button("Show me my prediction pot!"):
                recommended_games = get_knn_recommendations(df, num_players, game_duration, game_theme, game_difficulty, game_age)
                recommended_games['bgg_url'] = recommended_games['bgg_url'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
                st.markdown('<div class="custom-input-label">Behold! The fruits of our divination. These games are tailored to your desires, my dear!</div>', unsafe_allow_html=True)
                st.write(" ")
                st.markdown("<div class='styled-table'>" + recommended_games.rename(columns={'names': 'Title', 'bgg_url': 'Link to the description'}).to_html(classes='styled-table', escape=False, index=False) + "</div>", unsafe_allow_html=True)
                show_recommendations_button = True

                if st.button("Again!"):
                    st.rerun()

