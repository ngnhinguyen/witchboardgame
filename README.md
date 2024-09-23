# witchboardgame?! 🎲🔮

Willkommen bei witchboardgame?!, einer interaktiven Streamlit-App, die dir personalisierte Brettspiel-Empfehlungen basierend auf deinen Vorlieben bietet. Diese technische Anleitung hilft dir dabei, die App einfach einzurichten und zu starten.

# Inhaltsverzeichnis
1. Projektbeschreibung
2. Voraussetzungen
3. Installation
   1. Repository klonen
   2. Virtuelle Umgebung einrichten
   3. Abhängigkeiten installieren
4. Anwendung starten
5. Projektstruktur
6. Daten und Dateien

## Projektbeschreibung
witchboardgame?! ist eine Python-basierte Webanwendung, die mit Streamlit entwickelt wurde. Sie nutzt maschinelles Lernen, um individuelle Brettspiel-Empfehlungen zu geben. Basierend auf deinen Antworten auf verschiedene Fragen zur Spielerzahl, Spieldauer, Thema und Schwierigkeitsgrad, zeigt die App passende Spiele.

## Voraussetzungen
Bevor du mit der Installation beginnst, stelle sicher, dass du die folgenden Voraussetzungen erfüllst:

Python 3.7 oder höher: Die App ist in Python geschrieben und benötigt eine kompatible Python-Version.
Git: Um das Repository zu klonen.
Internetverbindung: Für das Herunterladen der benötigten Pakete und das Ausführen der Streamlit-App.

## Installation
Folge diesen Schritten, um witchboardgame?! auf deinem lokalen Rechner einzurichten:

## 1. Repository klonen
Zuerst musst du das Repository auf deinen Computer klonen. Öffne dazu dein Terminal und führe den folgenden Befehl aus:


    git clone https://github.com/ngnhinguyen/witchboardgame

Wechsle anschließend in das Projektverzeichnis:

    cd witchboardgame
    
## 2. Virtuelle Umgebung einrichten
Es wird empfohlen, eine virtuelle Umgebung zu verwenden, um Abhängigkeiten isoliert zu verwalten.
Mit bspw. conda:

    conda create --name witchboardgame python=3.9

Aktiviere die virtuelle Umgebung mit conda:


    conda activate witchboardgame


Oder nutze bspw. venv:

    python -m venv env

Aktiviere die virtuelle Umgebung:

Windows:

    env\Scripts\activate

macOS/Linux:

    source env/bin/activate

## 3. Abhängigkeiten installieren
Installiere die benötigten Python-Pakete mit pip:

    pip install -r requirements.txt

Hinweis: Zusätzliche Pakete wie design.styles, model.trainvalidation usw. sollten im Projekt enthalten sein. Stelle sicher, dass alle Modulpfade korrekt sind.
Es könnte einige Minuten dauern, bis die Abhängigkeiten installiert sind.

## Anwendung starten
Sobald alle Abhängigkeiten installiert sind, kannst du die Streamlit-App starten:

    streamlit run boardgameapp.py
    
Nach Ausführung dieses Befehls öffnet sich dein Standard-Webbrowser automatisch und zeigt die WitchBoardGame?!-App an. Falls sich der Browser nicht automatisch öffnet, folge dem im Terminal angezeigten lokalen URL (z.B., http://localhost:8501).
Es könnte einige Minuten dauern, bis die Anwendung startet. 

Hinweis: 
Klicke auf die drei Punkte oben rechts neben dem Button Deploy, dann auf Settings, unter Choose app theme, colors and fonts wähle "Dark" aus. Damit siehst du die App wie beabsichtigt. Auch ohne diese Änderung funktioniert die App, jedoch ist es unter Dark mode wesentlich angenehmer.


## Projektstruktur
Das Projekt ist wie folgt strukturiert:

boardgameapp.py: Hauptanwendungsskript.

design/: Enthält UI-Designs und Style-Dateien.
Darunter fallen 
- app_ui.py: Enthält alle UI Einstellungen der App.
- game_ui.py: Eine frühere Version von app_ui.py
- styles.py: Enthält den Code für den Stil und Layout der App.

model/: Beinhaltet die Modelle und Datenvorverarbeitungsskripte.
Darunter gehören
- cross_validation.py: Implementierung des Cross-Validation.
- knn.py: Implementierung des kNN- Modells.
- preprocess.py: Enthält die Datenvorverarbeitung des Datensatzes.
- trainvalidation.py: Implementierung des Train-Validation-Test-Splits.

bgg_db_1806.csv: Datensatz der Brettspiele.

hail-126903.mp3: Audiodatei für die App.

## Daten und Dateien
Stelle sicher, dass die folgenden Dateien im Projektverzeichnis vorhanden sind:

bgg_db_1806.csv: Die CSV-Datei enthält die Brettspieldaten. Diese Datei wird für die Datenvorverarbeitung und Empfehlungen verwendet.
hail-126903.mp3: Eine Audiodatei, die in der App abgespielt wird.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Viel Spaß mit witchboardgame?!! 🧙‍♀️🎲
