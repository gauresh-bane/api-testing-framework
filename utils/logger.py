# Utilities for logging

import logging
import os
from datetime import datetime
from config.settings import Config

def setup_logger(name: str) -> logging.Logger:
    """Setup logger with file and console handlers"""
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, Config.LOG_LEVEL, "logging.INFO"))
    
    # Create logs directory if it doesn't exist
    logs_dir = "./logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    # File handler
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_handler = logging.FileHandler(f"{logs_dir}/test_{timestamp}.log")
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, Config.LOG_LEVEL.split('.')[-1], "logging.INFO"))
    
    # Formatter
    formatter = logging.Formatter(Config.LOG_FORMAT)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger