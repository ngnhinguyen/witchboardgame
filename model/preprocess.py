import pandas as pd

def preprocess_data(filepath):
    df = pd.read_csv(filepath)

    # Kriegsspiele und weiteres entfernen
    war_keywords = ['War', 'Wargame', 'Conflict', 'Post-Napoleonic', 'Prehistoric', 'Napoleonic', 'Miscellaneous Game Accessory', 'Traditional Card Games']
    filtered_rows = [row for index, row in df.iterrows() if not any(keyword in row['category'] for keyword in war_keywords)]
    df = pd.DataFrame(filtered_rows)

    #Spieldauer in Wertebereiche teilen für alle Spiele in Spalte avg time
    def categorize_duration(avg_time):
        if avg_time <= 30:
            return '0-30'
        elif avg_time <= 60:
            return '30-60'
        elif avg_time <= 120:
            return '60-120'
        else:
            return '120+'
    df['duration_category'] = df['avg_time'].apply(categorize_duration)

  # Hauptkategorien der Spielmechaniken und Spielthemen extrahieren
    df['main_mechanic'] = df['mechanic'].apply(lambda x: x.split(',')[0])
    df['main_theme'] = df['category'].apply(lambda x: x.split(',')[0])

    #Duplikate entfernen in aufsteigender reihenfolge mit sorted()
    #spalte ['main_mechanic'] und main theme wird als df zurückgegeben
    #dropa() entfernt alle NaN Werte (ungültigen Werte) der Spalte
    #unique() gibt nur eindeutige Werte der Spalte zurück = keine Duplikate
    unique_mechanics = sorted(df['main_mechanic'].dropna().unique())
    unique_themes = sorted(df['main_theme'].dropna().unique())
    #Schwierigkeit kategorisieren nach Werten
    def categorize_difficulty(weight):
        if 1 <= weight < 2:
            return '1'
        elif 2 <= weight < 3:
            return '2'
        elif 3 <= weight < 4:
            return '3'
        elif 4 <= weight < 5:
            return '4'
        else:
            return '5'
        #hier wichtig: 'weight' statt 'weight category!
    df['weight'] = df['weight'].apply(categorize_difficulty)
    #Mindestalter kategorisieren
    def categorize_age(age):
        if age < 6:
            return '0'
        elif 6 <= age < 12:
            return '6'
        elif 12 <= age < 16:
            return '12'
        elif 16 <= age < 18:
            return '16'
        else:
            return '18'
    df['age'] = df['age'].apply(categorize_age)

    return df, unique_mechanics, unique_themes





