from utils.charts import (
    create_prediction_chart_data,
    create_risk_profile
)



sample = {


"Distraction_Level":"High",

"Academic_Impact_Level":"Medium",

"Social_Impact_Level":"Low",

"Focus_Level":"High"

}



print(
    create_prediction_chart_data(sample)
)



print()



print(
    create_risk_profile(sample)
)