"""
=====================================================
Vercel Serverless Entry Point
Digital Distraction Behaviour Analysis System
=====================================================
"""

import os
import sys

# Ensure the root project directory is available on Python path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app import app

# Expose WSGI application object for Vercel
if __name__ == "__main__":
    app.run()
