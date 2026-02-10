"""Configuration module for the solution."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
TIMEOUT = int(os.getenv("TIMEOUT", "30"))

# API Configuration
API_KEY = os.getenv("API_KEY", "")

# Database Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "solution_db")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

# Logging configuration
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "solution.log"

# Feature flags
ENABLE_CACHE = os.getenv("ENABLE_CACHE", "True").lower() == "true"
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "True").lower() == "true"
