"""
Logging utility for the bot.
"""

import logging
import sys
import os

def setup_logging():
    """Setup logging configuration."""
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    logger = logging.getLogger("telegram_bot")
    logger.info("Logging configured successfully")
    return logger

def get_logger(name: str):
    """Get a logger instance."""
    return logging.getLogger(name)