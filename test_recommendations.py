"""
=====================================================
Recommendation Engine
Digital Distraction Behaviour Analysis System
=====================================================

Purpose:
- Generate behavioural recommendations
- Generate assessment summary
- Provide clean output for Flask result page

=====================================================
"""



# =====================================================
# RECOMMENDATION GENERATOR
# =====================================================


def generate_recommendations(
        distraction,
        academic,
        social,
        focus
):


    recommendations = []



    # =================================================
    # DIGITAL DISTRACTION ANALYSIS
    # =================================================


    distraction_level = str(
        distraction
    ).lower()



    if distraction_level in [
        "high",
        "very high"
    ]:


        recommendations.append(

            "Create dedicated study sessions without smartphone interruptions."

        )


        recommendations.append(

            "Disable unnecessary notifications during important academic activities."

        )


        recommendations.append(

            "Avoid frequently switching between learning and entertainment applications."

        )


    elif distraction_level in [
        "medium",
        "moderate"
    ]:


        recommendations.append(

            "Monitor smartphone usage during study periods and maintain planned breaks."

        )


    else:


        recommendations.append(

            "Your digital usage behaviour appears controlled. Continue maintaining this balance."

        )





    # =================================================
    # ACADEMIC IMPACT ANALYSIS
    # =================================================


    academic_level = str(
        academic
    ).lower()



    if academic_level in [
        "high",
        "very high",
        "negative"
    ]:


        recommendations.append(

            "Develop a structured academic routine to reduce delays caused by digital distractions."

        )


    else:


        recommendations.append(

            "Continue maintaining consistent academic preparation habits."

        )






    # =================================================
    # SOCIAL IMPACT ANALYSIS
    # =================================================


    social_level = str(
        social
    ).lower()



    if social_level in [
        "high",
        "very high",
        "negative"
    ]:


        recommendations.append(

            "Maintain a healthy balance between online activities and face-to-face interactions."

        )





    # =================================================
    # FOCUS ANALYSIS
    # =================================================


    focus_level = str(
        focus
    ).lower()



    if focus_level in [
        "low",
        "very low",
        "poor"
    ]:


        recommendations.append(

            "Practice focused study sessions in a distraction-free environment."

        )


        recommendations.append(

            "Improve self-regulation by reducing unnecessary phone checking habits."

        )


    else:


        recommendations.append(

            "Continue strengthening your concentration and self-management skills."

        )






    # =================================================
    # REMOVE DUPLICATES
    # =================================================


    final_list = []



    for item in recommendations:


        if item not in final_list:


            final_list.append(item)





    return final_list






# =====================================================
# SUMMARY GENERATOR
# =====================================================


def generate_summary(
        distraction,
        academic,
        social,
        focus
):


    summary = (

        f"The assessment indicates a {distraction} "
        f"digital distraction behaviour pattern. "

        f"The academic impact level is {academic}. "

        f"The social impact level is {social}. "

        f"The focus and self-regulation level is {focus}."

    )


    return summary