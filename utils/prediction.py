"""
=====================================================
Prediction Engine
Digital Distraction Behaviour Analysis System

Final Model Wrapper
=====================================================
"""


import os
import joblib
import pandas as pd



# =====================================================
# MODEL LOCATION & LOADING
# =====================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "digital_distraction_final_model.pkl"
)


# =====================================================
# LOAD MODEL PACKAGE
# =====================================================

model_package = joblib.load(
    MODEL_PATH
)

MODEL_COLLECTION = model_package["models"]
FEATURE_COLUMNS = model_package["feature_columns"]


def get_model_info():
    return {
        "model_name": model_package.get("model_name", "Logistic Regression Distraction Predictor"),
        "version": model_package.get("version", "3.0"),
        "features": FEATURE_COLUMNS,
        "outputs": list(MODEL_COLLECTION.keys())
    }







# =====================================================
# RESPONSE ENCODING
# =====================================================


def encode_response(value):


    if value is None:
        return 0



    mappings = {


        # Frequency scale

        "Never":1,
        "Rarely":2,
        "Sometimes":3,
        "Often":4,
        "Always":5,


        # Agreement scale

        "Strongly Disagree":1,
        "Disagree":2,
        "Neutral":3,
        "Agree":4,
        "Strongly Agree":5,



        # Device categories

        "Mobile":1,
        "PC":2,
        "Both":3,


        # Usage time categories

        "Less than 2 hours":1.5,
        "2-4 hours":3,
        "4-6 hours":5,
        "More than 6 hours":7


    }



    return mappings.get(
        value,
        value
    )









# =====================================================
# PREPARE INPUT DATA
# =====================================================


def prepare_dataframe(user_input):



    processed = {}



    for feature in FEATURE_COLUMNS:


        value = user_input.get(
            feature,
            0
        )


        processed[feature] = encode_response(
            value
        )



    dataframe = pd.DataFrame(
        [processed]
    )



    return dataframe







# =====================================================
# MAIN PREDICTION FUNCTION
# =====================================================


def predict_behavior(user_input):



    dataframe = prepare_dataframe(
        user_input
    )



    results = {}





    for output_name, package in MODEL_COLLECTION.items():



        model = package["model"]


        encoder = package["encoder"]





        prediction_value = model.predict(
            dataframe
        )[0]



        # Convert numerical class back
        # into original label


        prediction_label = encoder.inverse_transform(
            [prediction_value]
        )[0]



        results[output_name] = prediction_label





    return results