import streamlit as st

##Datei wurde später in app_ui.py weiter ausgeführt und fortgesetzt

#musik laden
def load_music():
    audio_file = open('hail-126903.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', start_time=0)

def ask_favorite_game(df):
    # Anzeige des Textes im gleichen Stil
    st.markdown('<div class="custom-input-label">"Wie heißt dein Lieblingsbrettspiel?"</div>', unsafe_allow_html=True)
    # Eingabefeld für Lieblingsspiel
    favorite_game = st.text_input(' ')
    
    selected_game = None #wie null in Java, selected game erst ohne wert da kein spiel ausgewählt
    if favorite_game:
         #sucht im df spalte names nach input wert
        #case - groß,kleinschreibung wird nicht unterschieden
        #na false- ungültige bzw fehlende werte egal, nicht berücksichtigt
        filtered_games = df[df['names'].str.contains(favorite_game, case=False, na=False)]
        #wenn frame empty weil keine treffer dann spiel aussuchen
        if filtered_games.empty:#https://stackoverflow.com/questions/19828822/how-do-i-check-if-a-pandas-dataframe-is-empty
            st.markdown('<div class="custom-input-label">"Kein Spiel gefunden. Bitte wähle ein Spiel aus der Liste unten, das deinem Lieblingsspiel am ähnlichsten ist:"</div>', unsafe_allow_html=True)
            all_games = df['names'].dropna().unique()
            selected_game = st.selectbox("Ähnlichstes Spiel:", all_games) #alle spiele mit unterschiedlichen werten speichern in allgames
        else:
            st.markdown('<div class="custom-input-label">Ich habe diese Spiele gefunden:</div>', unsafe_allow_html=True)
            game_options = filtered_games['names'].dropna().unique()
            selected_game = st.selectbox("Wähle ein Spiel:", game_options)
    
    return selected_game

def ask_preferences(df, unique_themes):
    # Frage nach Anzahl der Spieler
    st.markdown('<div class="custom-input-label">"Mit wie vielen Personen spielst du gerne Brettspiele?"</div>', unsafe_allow_html=True)
    num_players = st.selectbox('', sorted(df['min_players'].dropna().unique()))
    
    # Frage nach Spieldauer
    st.markdown('<div class="custom-input-label">"Wie lange sollte ein Spiel dauern (Durchschnittszeit in Minuten)?"</div>', unsafe_allow_html=True)
    game_duration = st.selectbox('', ['0-30', '30-60', '60-120', '120+'])
    
    # Frage nach Spielthemen
    st.markdown('<div class="custom-input-label">"Welche Kategorie bevorzugst du?"</div>', unsafe_allow_html=True)
    game_theme = st.selectbox('', unique_themes)
    
    # Frage nach Schwierigkeitsgrad
    st.markdown('<div class="custom-input-label">"Welchen Schwierigkeitsgrad bevorzugst du? (1 sehr leicht, 2 leicht, 3 medium, 4 schwer, 5 sehr schwer)"</div>', unsafe_allow_html=True)
    game_difficulty = st.selectbox('', sorted(df['weight'].dropna().unique()))
    
    # Frage nach Mindestalter
    st.markdown('<div class="custom-input-label">"Für welches Mindestalter soll das Spiel geeignet sein?"</div>', unsafe_allow_html=True)
    game_age = st.selectbox('', sorted(df['age'].dropna().unique()))
    
    return num_players, game_duration, game_theme, game_difficulty, game_age
