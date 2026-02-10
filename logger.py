"""Logging configuration and utilities."""

import logging
import sys

# Basic logger setup (no external configuration dependencies)
def setup_logger(name=__name__):
    """Set up logger with console handler.
    
    Args:
        name: Logger name
        
    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Console handler
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger


# Create module-level logger
logger = setup_logger(__name__)
