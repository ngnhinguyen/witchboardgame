import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def get_recommendations(df, num_players, game_duration, game_mechanics, game_theme, game_difficulty, game_age):
    # Features und Zielvariable
       #zielvariable/target ist 'names'
        #features sind 'min_players', 'max_players', 'duration_category', 'main_mechanic', 'category', 'weight', 'age'    
    X = df[['min_players', 'max_players', 'duration_category', 'main_mechanic', 'category', 'weight', 'age']]
    y = df['names']
    
    # pandas Methode get_dummies um Variablen in numerische Form zu konvertieren(0, 1) 
    X = pd.get_dummies(X, columns=['duration_category', 'main_mechanic', 'category', 'weight', 'age'])
    
    # Benutzereingaben
    # erinnerung: np.array für KNN sind numerisce Eingabedaten wichtig!!!!
        # benutzereingaben sind input
    input_vector = np.array([[
        num_players, num_players, game_duration, game_mechanics, game_theme, game_difficulty, game_age
    ]])
    input_vector = pd.DataFrame(input_vector, columns=['min_players', 'max_players', 'duration_category', 'main_mechanic', 'category', 'weight', 'age'])
    input_vector = pd.get_dummies(input_vector, columns=['duration_category', 'main_mechanic', 'category', 'weight', 'age'])
    
    # Anpassen des Input-Vektors:   #input wird an x angepasst, dass beide datensätze gleiche spalten haben und
        # fehlende spalten mit 0 auffüllen
    input_vector = input_vector.reindex(columns=X.columns, fill_value=0)
    
    # Datenaufteilung in Training und Testen
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=10)
    
    # Random Forest Modell trainieren
    rf = RandomForestClassifier(n_estimators=11, random_state=10)
    rf.fit(X_train, y_train)
    
    # Vorhersagen basierend auf den Benutzereingaben
    recommendations = rf.predict(input_vector)
    
    # Empfohlene Spiele anzeigen
    recommended_games = df[df['names'].isin(recommendations)]
    
    return recommended_games[['names', 'min_players', 'max_players', 'avg_time', 'main_mechanic', 'category', 'weight', 'age']]
