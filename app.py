"""
=====================================================
Digital Distraction Behaviour Analysis System
Main Flask Application
=====================================================
"""

import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify
)

# =====================================================
# INTERNAL MODULES
# =====================================================

from utils.prediction import (
    predict_behavior,
    get_model_info
)

from utils.recommendations import (
    generate_recommendations,
    generate_summary
)

from utils.database import (
    save_prediction,
    get_prediction_history,
    get_prediction_by_id,
    clear_history,
    initialize_database
)

from utils.charts import (
    generate_dashboard_data
)

# =====================================================
# APPLICATION CONFIGURATION
# =====================================================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "digital-distraction-system-secret-key"
)

# Initialize database
try:
    initialize_database()
except Exception as e:
    print(f"Warning: Database initialization deferred: {e}")


# =====================================================
# HOME & STATUS ROUTES
# =====================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "system": "Digital Distraction Behaviour Analysis System",
        "version": "V3.0"
    })


# =====================================================
# PREDICTION ROUTE
# =====================================================

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # -------------------------------------
        # Collect user input
        # -------------------------------------
        form_data = request.form.to_dict()

        # -------------------------------------
        # Model Prediction
        # -------------------------------------
        predictions = predict_behavior(form_data)

        # -------------------------------------
        # Extract categories
        # -------------------------------------
        distraction = predictions.get("Distraction_Level", "Unknown")
        academic = predictions.get("Academic_Impact_Level", "Unknown")
        social = predictions.get("Social_Impact_Level", "Unknown")
        focus = predictions.get("Focus_Level", "Unknown")

        result = {
            "distraction": distraction,
            "academic": academic,
            "social": social,
            "focus": focus
        }

        # -------------------------------------
        # Recommendations
        # -------------------------------------
        recommendations = generate_recommendations(
            distraction,
            academic,
            social,
            focus
        )

        # -------------------------------------
        # Summary
        # -------------------------------------
        summary = generate_summary(
            distraction,
            academic,
            social,
            focus
        )

        # -------------------------------------
        # Chart Data
        # -------------------------------------
        chart_data = generate_dashboard_data(predictions)

        # -------------------------------------
        # Save History
        # -------------------------------------
        try:
            save_prediction(
                form_data,
                predictions,
                recommendations
            )
        except Exception as db_err:
            print(f"Database save warning: {db_err}")

        # -------------------------------------
        # Result Page
        # -------------------------------------
        return render_template(
            "result.html",
            result=result,
            predictions=predictions,
            summary=summary,
            explanation=summary,
            recommendations=recommendations,
            chart_data=chart_data
        )

    except Exception as error:
        print("\nPREDICTION ERROR:", error)
        return render_template("500.html", error=str(error)), 500


# =====================================================
# DASHBOARD PAGES
# =====================================================

@app.route("/behaviour")
def behaviour():
    return render_template("behaviour.html")


@app.route("/risk-profile")
def risk_profile():
    history = get_prediction_history()
    latest = None
    if history:
        latest = history[0]["prediction"]

    return render_template(
        "risk_profile.html",
        prediction=latest
    )


@app.route("/history")
def history():
    records = get_prediction_history()
    return render_template(
        "history.html",
        records=records
    )


@app.route("/history/<int:id>")
def history_detail(id):
    record = get_prediction_by_id(id)
    return render_template(
        "history_detail.html",
        record=record
    )


@app.route("/clear-history")
def clear_history_route():
    clear_history()
    return redirect(url_for("history"))


@app.route("/wellness")
def wellness():
    history = get_prediction_history()
    latest = None
    if history:
        latest = history[0]

    return render_template(
        "wellness.html",
        latest=latest
    )


@app.route("/research")
def research():
    return render_template("research.html")


# =====================================================
# ERROR HANDLERS
# =====================================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html", error=str(error)), 500


# =====================================================
# RUN SERVER (FOR LOCAL DEVELOPMENT)
# =====================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )