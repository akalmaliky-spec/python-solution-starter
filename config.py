"""Configuration module for the solution."""

import os

# Application settings (no external dependencies)
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
TIMEOUT = int(os.getenv("TIMEOUT", "30"))

# Feature flags
ENABLE_CACHE = os.getenv("ENABLE_CACHE", "True").lower() == "true"
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "True").lower() == "true"
