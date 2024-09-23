import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

#Hier werden alle Spiele angeschaut und es wird nach Spielen mit passenden Merkmalen geschaut, die zu den Anforderungen (Antworten der Fragen) passen
def get_knn_recommendations(df, num_players, game_duration, game_theme, game_difficulty, game_age):
    X = df[['min_players', 'max_players', 'duration_category', 'category', 'weight', 'age']] #Features
    y = df['names'] #Zielvariable/ Target
    
    # Pandas Methode get_dummies um kategorische Variablen in numerische Form zu konvertieren (0, 1) für KNN Modell ((One-Hot-Encoding))
    X = pd.get_dummies(X, columns=['duration_category', 'category', 'weight', 'age'])
    
    #Feature-Skalierung hinzufügen mit Standardscaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Erinnerung: np.array für KNN sind numerische Eingabedaten wichtig!!!!
    # Benutzereingabe vorbereiten: Features werden in input_vector gespeichert
    input_vector = np.array([[
        num_players, num_players, game_duration, game_theme, game_difficulty, game_age, 
    ]])
    input_vector = pd.DataFrame(input_vector, columns=['min_players', 'max_players', 'duration_category', 'category', 'weight', 'age'])
    input_vector = pd.get_dummies(input_vector, columns=['duration_category','category', 'weight', 'age'])
    
    # Input wird an X angepasst, dass beide Datensätze gleiche Spalten haben und fehlende Spalten mit 0 auffüllen
    input_vector = input_vector.reindex(columns=X.columns, fill_value=0)
    
    # KNN Modell mit n=5 erstellen und mit skalierten Daten trainieren
    knn = KNeighborsClassifier(n_neighbors=5)
    #Skalierte X Features verwenden
    knn.fit(X_scaled, y)
    
    #knn berechnet, welche 5 Spiele am ähnlichsten zu den Benutzereingaben sind. Dies geschieht durch Berechnung der Distanzen im Merkmalsraum.
    recommendations = knn.kneighbors(input_vector, return_distance=False)
    recommended_games = df.iloc[recommendations[0]]
    
    return recommended_games[['names','bgg_url']]

#Hier wird nach Merkmalen der Lieblingsspiele geschaut und Empfehlungen ausgegeben für Spiele, die ähnliche Merkmale haben
#df ist hier Liste von Spielen und favorite_games ist hier die Eingabe von einem/zwei/drei Lieblingsspielen
def get_recommendations_by_favorite_games(df, favorite_games):
    X = df[['names', 'min_players', 'max_players', 'duration_category', 'category', 'weight', 'age']]
    y = df['names']

    # Auswahl der Zeilen für die Lieblingsspiele
    # Daten zu den Lieblingsspielen werden aus dem dataframe gefiltert
    favorite_games_df = df[df['names'].isin(favorite_games)]

    if favorite_games_df.empty:
        return pd.DataFrame()  # Keine Spiele gefunden

    # KNN-Modell auf den gesamten Datensatz anpassen
    X = pd.get_dummies(X, columns=['duration_category', 'category', 'weight', 'age'])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X.drop(columns=['names']))

    # Lieblingsspiele Vektor extrahieren
    # Aus skalierten Daten werden die Merkmalsvektoren der Lieblingsspiele extrahiert
    favorite_games_vectors = X[X['names'].isin(favorite_games)].drop(columns=['names'])

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_scaled, y)

    #knn berechnet, welche Spiele am ähnlichsten zu den Lieblingsspielen sind
    #Die ähnlichsten Spiele werden basierend auf den kleinsten Distanzen ausgewählt und zurückgegeben
    recommendations = knn.kneighbors(favorite_games_vectors, return_distance=False)
    recommended_games = df.iloc[recommendations[0]]

    return recommended_games[['names', 'bgg_url']]

