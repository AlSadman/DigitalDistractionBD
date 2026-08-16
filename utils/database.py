"""
=====================================================
Database System
Digital Distraction Behaviour Analysis System
=====================================================
"""

import sqlite3
import os
import json
import shutil
from datetime import datetime


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


def get_database_path():
    """
    Returns the appropriate SQLite database path.
    If on Vercel / serverless environment (where root fs is read-only),
    uses /tmp/history.db and seeds it from bundled database if available.
    """
    custom_path = os.environ.get("DATABASE_PATH")
    if custom_path:
        return custom_path

    # Check if running on Vercel or AWS Lambda / read-only serverless environment
    is_vercel = os.environ.get("VERCEL") == "1" or os.environ.get("AWS_LAMBDA_FUNCTION_NAME") is not None

    if is_vercel:
        tmp_db = os.path.join("/tmp", "history.db")
        bundled_db = os.path.join(BASE_DIR, "database", "history.db")

        # If tmp db doesn't exist yet but bundled db does, copy bundled data
        if not os.path.exists(tmp_db) and os.path.exists(bundled_db):
            try:
                shutil.copy2(bundled_db, tmp_db)
            except Exception:
                pass
        return tmp_db

    # Default local path
    db_folder = os.path.join(BASE_DIR, "database")
    os.makedirs(db_folder, exist_ok=True)
    return os.path.join(db_folder, "history.db")


def initialize_database():
    db_path = get_database_path()
    db_dir = os.path.dirname(db_path)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS assessments
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT,
            input_data TEXT,
            prediction_data TEXT,
            recommendations TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def save_prediction(
        input_data,
        prediction,
        recommendations
):
    initialize_database()
    db_path = get_database_path()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO assessments
        (
            created_at,
            input_data,
            prediction_data,
            recommendations
        )
        VALUES (?,?,?,?)
        """,
        (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            json.dumps(input_data),
            json.dumps(prediction),
            json.dumps(recommendations)
        )
    )

    conn.commit()
    conn.close()


def get_prediction_history():
    initialize_database()
    db_path = get_database_path()

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM assessments
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()
    conn.close()

    history = []
    for row in rows:
        try:
            history.append(
                {
                    "id": row["id"],
                    "date": row["created_at"],
                    "input": json.loads(row["input_data"]),
                    "prediction": json.loads(row["prediction_data"]),
                    "recommendations": json.loads(row["recommendations"])
                }
            )
        except Exception:
            continue

    return history


def get_prediction_by_id(record_id):
    history = get_prediction_history()
    for item in history:
        if item["id"] == record_id:
            return item
    return None


def clear_history():
    initialize_database()
    db_path = get_database_path()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM assessments")

    conn.commit()
    conn.close()