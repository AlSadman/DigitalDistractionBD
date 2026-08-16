"""
Recommendation Engine
Digital Distraction Behaviour Analysis System
"""


def generate_recommendations(
        distraction,
        academic,
        social,
        focus
):

    recommendations = []


    distraction = str(distraction).lower()
    academic = str(academic).lower()
    social = str(social).lower()
    focus = str(focus).lower()



    # Distraction recommendations

    if distraction in ["high", "very high"]:

        recommendations.append(
            "Create dedicated study sessions without smartphone interruptions."
        )

        recommendations.append(
            "Disable unnecessary notifications during study periods."
        )

    elif distraction in ["medium", "moderate"]:

        recommendations.append(
            "Monitor smartphone usage during study sessions."
        )

    else:

        recommendations.append(
            "Continue maintaining balanced digital habits."
        )



    # Academic recommendations

    if academic in ["high", "very high", "negative"]:

        recommendations.append(
            "Develop a structured academic routine to reduce digital interruptions."
        )



    # Social recommendations

    if social in ["high", "very high", "negative"]:

        recommendations.append(
            "Maintain balance between online activities and real-world interaction."
        )



    # Focus recommendations

    if focus in ["low", "very low", "poor"]:

        recommendations.append(
            "Practice focused study sessions in a distraction-free environment."
        )

    else:

        recommendations.append(
            "Continue improving concentration and self-regulation skills."
        )



    return recommendations






def generate_summary(
        distraction,
        academic,
        social,
        focus
):

    return (

        f"The assessment indicates a {distraction} "
        f"digital distraction behaviour pattern. "

        f"The academic impact level is {academic}. "

        f"The social impact level is {social}. "

        f"The focus and self-regulation level is {focus}."

    )