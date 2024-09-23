from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
from design.styles import load_global_styles, load_welcome_page_styles, load_explanation_page_styles, load_recommendations_page_styles
from model.trainvalidation import get_recommendations
from model.knn import get_knn_recommendations 
from model.preprocess import preprocess_data
from design.app_ui import show_welcome_page, show_explanation_page, show_recommendations

load_global_styles()

#variable "page" nicht vorhanden, dann wird anwendung erst gestartet
#bei starten der anwendung ist session state variable welcome
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
#je nach wert der session state variable öffnet sich eine seite 
if st.session_state.page == 'welcome':
    show_welcome_page()
elif st.session_state.page == 'explanation':
    show_explanation_page()
else:
    show_recommendations()




  