"""
Base settings for the API Orchestration Layer.

This file defines global configurations, environment loading, and shared constants.
All names follow strict technical conventions according to workspace rules.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_API_BASE_URL: str = "https://api.openai.com/v1"

settings = Settings()
