"""Logging configuration and utilities."""

import logging
import sys
from config import LOG_LEVEL, LOG_FORMAT, LOG_FILE, ENABLE_LOGGING


def setup_logger(name=__name__):
    """Set up logger with file and console handlers.
    
    Args:
        name: Logger name
        
    Returns:
        Logger instance
    """
    if not ENABLE_LOGGING:
        return logging.getLogger(name)
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_LEVEL))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, LOG_LEVEL))
    console_formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # File handler
    try:
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(getattr(logging, LOG_LEVEL))
        file_formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    except (IOError, OSError) as e:
        logger.warning(f"Could not create log file: {e}")
    
    return logger


# Create module-level logger
logger = setup_logger(__name__)
