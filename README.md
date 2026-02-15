# witchboardgame?! 🎲🔮

Welcome to witchboardgame?!, an interactive Streamlit app that provides personalized board game recommendations based on your preferences. This technical guide will help you easily set up and launch the app.

# Table of Contents
1. Project Description
2. Requirements
3. Installation
   1. Clone Repository
   2. Set Up Virtual Environment
   3. Install Dependencies
4. Start the Application
5. Project Structure
6. Data and Files

## Project Description
witchboardgame?! is a Python-based web application developed with Streamlit. It uses machine learning to provide individual board game recommendations. Based on your answers to various questions about number of players, game duration, theme, and difficulty level, the app displays suitable games.

## Requirements
Before starting the installation, make sure you meet the following requirements:

Python 3.7 or higher: The app is written in Python and requires a compatible Python version.
Git: To clone the repository.
Internet connection: For downloading the required packages and running the Streamlit app.

## Installation
Follow these steps to set up witchboardgame?! on your local machine:

## 1. Clone Repository
First, you need to clone the repository to your computer. Open your terminal and run the following command:

    git clone https://github.com/ngnhinguyen/witchboardgame

Then switch into the project directory:

    cd witchboardgame
    
## 2. Set Up Virtual Environment
It is recommended to use a virtual environment to manage dependencies in isolation.
Using, for example, conda:

    conda create --name witchboardgame python=3.9

Activate the virtual environment with conda:

    conda activate witchboardgame

Or use, for example, venv:

    python -m venv env

Activate the virtual environment:

Windows:

    env\Scripts\activate

macOS/Linux:

    source env/bin/activate

## 3. Install Dependencies
Install the required Python packages using pip:

    pip install -r requirements.txt

Note: Additional packages such as design.styles, model.trainvalidation, etc., should be included in the project. Make sure that all module paths are correct.
It may take several minutes until the dependencies are installed.

## Start the Application
Once all dependencies are installed, you can start the Streamlit app:

    streamlit run boardgameapp.py
    
After executing this command, your default web browser will automatically open and display the WitchBoardGame?! app. If the browser does not open automatically, follow the local URL shown in the terminal (e.g., http://localhost:8501).
It may take several minutes until the application starts. 

Note: 
Click on the three dots in the top right next to the Deploy button, then click on Settings. Under Choose app theme, colors and fonts select "Dark". This allows you to see the app as intended. The app will also work without this change, but it is much more pleasant in Dark mode.

## Project Structure
The project is structured as follows:

boardgameapp.py: Main application script.

design/: Contains UI designs and style files.
This includes 
- app_ui.py: Contains all UI settings of the app.
- game_ui.py: An earlier version of app_ui.py
- styles.py: Contains the code for the style and layout of the app.

model/: Contains the models and data preprocessing scripts.
This includes
- cross_validation.py: Implementation of cross-validation.
- knn.py: Implementation of the kNN model.
- preprocess.py: Contains the data preprocessing of the dataset.
- trainvalidation.py: Implementation of the train-validation-test split.

bgg_db_1806.csv: Board game dataset.

hail-126903.mp3: Audio file for the app.

## Data and Files
Make sure the following files are present in the project directory:

bgg_db_1806.csv: The CSV file contains the board game data. This file is used for data preprocessing and recommendations.
hail-126903.mp3: An audio file that is played in the app.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Have fun with witchboardgame?!! 🧙‍♀️🎲
