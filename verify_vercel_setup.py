"""
Comprehensive Verification Script for Vercel Deployment Readiness
"""

import os
import sys
import unittest

# Set test environment
os.environ["SECRET_KEY"] = "test-secret-key"

# 1. Test importing serverless entrypoint
try:
    from api.index import app
    print("SUCCESS: api.index imported successfully.")
except Exception as e:
    print(f"FAILED: Could not import api.index: {e}")
    sys.exit(1)


class TestVercelSetup(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_routes_get(self):
        routes = [
            ("/", 200),
            ("/health", 200),
            ("/behaviour", 200),
            ("/risk-profile", 200),
            ("/history", 200),
            ("/wellness", 200),
            ("/research", 200),
        ]
        for route, expected_code in routes:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(
                    response.status_code,
                    expected_code,
                    f"Route {route} returned status {response.status_code}"
                )
                print(f"PASS: GET {route} -> {response.status_code}")

    def test_prediction_post(self):
        sample_data = {
            "Academic_Stress": "3",
            "Screen_Time_Usage": "2-4 hours",
            "Notification_Checking_Frequency": "Often",
            "Device_Usage_Type": "Both",
            "Distraction_Level": "Often",
            "Focus_Loss_Frequency": "Sometimes",
            "Sleep_Interruption": "Rarely",
            "Study_Interruption": "Often"
        }

        response = self.client.post("/predict", data=sample_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Distraction", response.data)
        print("PASS: POST /predict returned 200 and rendered result page.")

    def test_history_and_clear(self):
        response = self.client.get("/clear-history", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        print("PASS: GET /clear-history redirected to history page.")

    def test_vercel_tmp_db(self):
        from utils.database import get_database_path, initialize_database, save_prediction, get_prediction_history
        os.environ["VERCEL"] = "1"
        try:
            db_path = get_database_path()
            self.assertTrue(db_path.startswith("/tmp") or "\\tmp" in db_path or "tmp" in db_path)
            initialize_database()
            save_prediction({"test": "1"}, {"Distraction_Level": "Low"}, ["Keep going"])
            history = get_prediction_history()
            self.assertTrue(len(history) >= 1)
            print("PASS: Vercel /tmp database simulation successful.")
        finally:
            os.environ.pop("VERCEL", None)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVercelSetup)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
