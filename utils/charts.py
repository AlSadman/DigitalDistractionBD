"""
=====================================================
Chart Data Generator
Digital Distraction Behaviour Analysis System
=====================================================

Purpose:
- Prepare data for result charts
- Prepare dashboard visualization data
- Support future research analytics

=====================================================
"""



# =====================================================
# LEVEL TO SCORE CONVERSION
# =====================================================


def level_to_score(level):


    level = str(level).lower()



    mapping = {


        "very low":20,

        "low":35,

        "medium":60,

        "moderate":60,

        "high":80,

        "very high":95

    }



    return mapping.get(
        level,
        50
    )






# =====================================================
# RESULT CHART DATA
# =====================================================


def create_prediction_chart_data(
        predictions
):


    labels = []

    values = []



    for key,value in predictions.items():


        labels.append(

            key.replace(
                "_",
                " "
            )

        )


        values.append(

            level_to_score(
                value
            )

        )



    return {


        "labels":labels,


        "values":values

    }








# =====================================================
# RISK PROFILE DATA
# =====================================================


def create_risk_profile(
        predictions
):


    profile = {}



    for key,value in predictions.items():


        profile[key] = {


            "level":value,


            "score":
            level_to_score(value)


        }



    return profile







# =====================================================
# RESEARCH INFORMATION
# =====================================================


def research_statistics():


    return {


        "dataset_size":1015,


        "feature_count":23,


        "analysis_categories":4,


        "model":
        "Logistic Regression Digital Distraction Behaviour Prediction System"


    }







# =====================================================
# MAIN DASHBOARD FUNCTION
# =====================================================


def generate_dashboard_data(
        predictions
):


    return {


        "prediction_chart":

            create_prediction_chart_data(
                predictions
            ),



        "risk_profile":

            create_risk_profile(
                predictions
            ),



        "research":

            research_statistics()

    }