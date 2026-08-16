import os


# ===============================
# APPLICATION CONFIGURATION
# ===============================

BASE_DIR = os.path.abspath(
    os.path.dirname(__file__)
)


# ===============================
# MODEL CONFIGURATION
# ===============================

MODEL_FOLDER = os.path.join(
    BASE_DIR,
    "model"
)


MODEL_PATH = os.path.join(
    MODEL_FOLDER,
    "digital_distraction_final_model.pkl"
)



# ===============================
# DATABASE CONFIGURATION
# ===============================

DATABASE_FOLDER = os.path.join(
    BASE_DIR,
    "database"
)


DATABASE_PATH = os.path.join(
    DATABASE_FOLDER,
    "history.db"
)



# ===============================
# FLASK SETTINGS
# ===============================

SECRET_KEY = (
    "digital_distraction_secure_key_2026"
)


DEBUG = True



# ===============================
# FEATURE CONFIGURATION
# ===============================


OUTPUT_LABELS = [

    "Distraction_Level",

    "Academic_Impact_Level",

    "Social_Impact_Level",

    "Focus_Level"

]



# ===============================
# SURVEY ENCODING
# ===============================


AGREEMENT_MAPPING = {

    "Strongly Disagree": 1,

    "Disagree": 2,

    "Neutral": 3,

    "Agree": 4,

    "Strongly Agree": 5

}



FREQUENCY_MAPPING = {

    "Never": 1,

    "Rarely": 2,

    "Sometimes": 3,

    "Often": 4,

    "Always": 5

}



DEVICE_MAPPING = [

    "Mobile",

    "PC",

    "Both"

]



# ===============================
# APP INFORMATION
# ===============================


APP_NAME = (

    "Digital Distraction "

    "Behaviour Analysis System"

)


VERSION = "V3.0"