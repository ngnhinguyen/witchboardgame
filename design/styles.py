import streamlit as st

def load_global_styles():
    font_css = '''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barriecito&display=swap');

    body * {
        font-family: "Barriecito", system-ui !important;
        font-weight: 400;
        font-style: normal;
        font-size: 21px;
    }
    </style>
    '''
    st.markdown(font_css, unsafe_allow_html=True)

def load_welcome_page_styles():
    page_bg_image = '''
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: black;
        background-size: cover;
    }
    '''
    st.markdown(page_bg_image, unsafe_allow_html=True)
    welcome_page_markdown = """
    <style>
    body {
        background-color: black;
        color: white;
        font-family: 'Press Start 2P', system-ui;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
        margin: 0;
        text-align: center;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .gif-container {
        margin-bottom: 20px;
    }
    .witchboardgame {
        font-size: 1.7em; 
        margin: 10px 0;
        width: 550px;
        color: white;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    </style>
    <div class="gif-container" style="display: flex; justify-content: center;">
        <img src="https://media.giphy.com/media/4KylpY41Wl1LiMuv9B/giphy.gif" alt="witchboardgame" width="200" height="230" style="margin: 20px">
    </div>
    <div class="centered">
        <h2 class="witchboardgame">witchboardgame?!</h2>
    </div>
    """
    st.markdown(welcome_page_markdown, unsafe_allow_html=True)

def load_explanation_page_styles():
    page_bg_foto = '''
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: black;
        background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_foto, unsafe_allow_html=True)
    
    explanation_page_markdown = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    body {
        background-color: black;
        color: white;
        font-family: 'Press Start 2P', system-ui;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin: 0;
        text-align: center;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .explanation-content {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 10px;
    }
    .explanation-content .image-container {
        flex: 1;
    }
    .explanation-content .text-container {
        flex: 2;
        background-color: white;
        color: black;
        padding: 20px;
        border-radius: 10px;
        font-size: 1em;
        margin-left: 20px;
    }
    .button-container {
        display: flex;
        margin-top: 20px;
    }
    .button {
        font-size: 1em; 
        background-color: white; 
        color: black; 
        border: none;
        border-radius: 5px;
        cursor: pointer; 
        padding: 10px 20px; 
    }
    </style>
    <div class="centered">
        <h2 class="witchboardgame">🪄 Oh, a familiar presence returns! </h2>
    </div>
    <div class="explanation-content">
        <div class="image-container">
            <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnd2cGgyeXJzNXQ1aGEzcWNreGVzazZqMHUwdzN4b3V5dGN6cHQ5OSZlcD12MV9pbnRlcm5naWZfYnlfaWQmY3Q9cw/H4ouioKgCtZ3b88gWL/giphy.webp" width="100%" height="100%" class="giphy-embed" allowFullScreen>
        </div>
        <div class="text-container">
             Welcome back to witchboardgame?!
             <br> <br /> Decades have passed since we last met. A cloud of doubt lingers around your aura...
             <br> <br />Behold! A hidden world of games awaits. I offer the modest collection, chosen with care, to suit your tastes.
            <br> <br /> Your fate hangs in the balance of these questions. Answer wisely.
            <br> <br /> Shall we embark on this magical journey together?
        </div>
    </div>
    """
    st.markdown(explanation_page_markdown, unsafe_allow_html=True)

def load_recommendations_page_styles():
    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/K6QMID53AFASXKQ6GJOQ6STHIQ.jpg&w=1440&impolicy=high_res");
        background-size: cover;
        
    }
    [data-testid="stMarkdownContainer"] h1, [data-testid="stTextInput"] label, [data-testid="stWrite"] label, [data-testid="stSelectbox"] label {
        color: white;
        font-weight: bold;
        font-size: 1.5em;
    }
    </style>
    '''
    font_css = '''
 
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown(font_css, unsafe_allow_html=True)
#https://www.html-seminar.de/css-border-rahmen.htm
#double = doppelt, dotted, ridge, inset, outset
    st.markdown("""
    <div style=" background:rgb(255,192,118));margin-bottom: 80px;
                border-radius: 20px;background: 
                radial-gradient(circle, rgba(255,192,118,1) 0%, rgba(255,70,0,1) 100%);
                border-color: black; text-shadow: 2px 2px 4px #000000; border-width: 1px; border-style: solid">
        <h1 style="color:rgba(255,249,243,1); text-align: center;">w i t c h b o a r d g a m e ?!</h1>
   
    """, unsafe_allow_html=True)    

    st.markdown("""
     <div style="background:rgb(255,192,118); border-radius: 20px;
                background: radial-gradient(circle, rgba(255,192,118,1) 0%, rgba(255,70,0,1) 100%);
                text-shadow: 2px 2px 4px #000000;
                border-color: black; text-shadow: 2px 2px 4px #000000;
                border-width: 1px; border-style: solid;
                text-align: center;
      </div>
        <div class="gif-container" style="display: flex; justify-content: center;">
        <img src="https://media.giphy.com/media/4KylpY41Wl1LiMuv9B/giphy.gif" alt="witchboardgame" width="100" height="115">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
     <div style="background:rgb(255,192,118); border-radius: 20px;margin-bottom: 20px;
                background: radial-gradient(circle, rgba(255,192,118,1) 0%, rgba(255,70,0,1) 100%);
                 text-shadow: 2px 2px 4px #000000;
                border-color: black; text-shadow: 2px 2px 4px #000000;
                border-width: 1px; border-style: solid">
        <h6 style="color: rgba(255,249,243,1); padding: 10px; text-align: center; ">Marvellous! Shall we summon a melody to soothe the spirits?</h6>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .custom-input-label {
            background: rgb(255,192,118);
            border-radius: 20px;
            background: radial-gradient(circle, rgba(255,192,118,1) 0%, rgba(255,70,0,1) 100%);
            text-shadow: 2px 2px 4px #000000;
            border-width: 1px; border-style: solid;
                border-color: black;
            color: rgba(255,249,243,1);
            padding: 10px;
            text-align: center;
            display: block;
            margin-bottom: 10px;
        }
        .stTextInput div[data-baseweb="input"] {
            background: rgb(255,192,118);
            border-radius: 20px;
            background: radial-gradient(circle, rgba(255,192,118,1) 0%, rgba(255,70,0,1) 100%);
            text-shadow: 2px 2px 4px #ff0000;
            border-color: black;
            border-width: 1px; border-style: solid;
            color: rgba(255,249,243,1);
            padding: 10px;
            text-align: center;
        }
        .warning-text {
            color: white;
            margin-top: px;
            background: red;
            border-radius: 20px;
            padding: 4px;
            text-align: center;
            margin-bottom: 25px;
        }
  
        </style>
        """, unsafe_allow_html=True)
    
    
    st.markdown(
            """
            <style>
        .styled-table {

        }
        .styled-table th, .styled-table td {
            text-align: center;
            padding: 8px; 
            font-size: 22px;
             width: 80/%; 
            margin: auto;
            border-collapse: collapse; 
            text-align: center;
            background: radial-gradient(circle, rgba(255,192,118,1) 0%, rgba(255,70,0,1) 100%);
            text-shadow: 2px 2px 4px #ff0000;
            border-color: black;
            border-width: 6px;
            border-style: dashed;
            color: white;
        }
        </style>
        """,
            unsafe_allow_html=True
        )
    
def load_button_styles():
    button_css = '''
    <style>
    .stButton > button {
        display: flex;
        margin: auto;
        justify-content: center;
        align-items: center;
        background-color: ;
        color: white;  
        border-radius: 10px; 
        padding: 10px 20px;
    }
    </style>
    '''
    st.markdown(button_css, unsafe_allow_html=True)

