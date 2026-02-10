"""Python Solution Starter Package.

A minimal Python starter kit with solution code template for competitive
programming, coding challenges, and algorithm development.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__url__ = "https://github.com/yourusername/python-solution-starter"

# Import main components
from logger import logger, setup_logger
from config import (
    DEBUG,
    LOG_LEVEL,
    API_KEY,
    DB_HOST,
    DB_PORT,
    DB_NAME,
    ENABLE_CACHE,
    ENABLE_LOGGING,
)
from utils import timer, memoize, read_input, parse_input, format_output
from main import solve, helper_function

__all__ = [
    "logger",
    "setup_logger",
    "timer",
    "memoize",
    "read_input",
    "parse_input",
    "format_output",
    "solve",
    "helper_function",
    "DEBUG",
    "LOG_LEVEL",
    "ENABLE_CACHE",
    "ENABLE_LOGGING",
]
