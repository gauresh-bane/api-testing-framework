# Configuration management

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    
    # API Configuration
    API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
    
    # Test Configuration
    TEST_DATA_PATH = os.getenv("TEST_DATA_PATH", "data/test_data.json")
    
    # Report Configuration
    REPORT_PATH = os.getenv("REPORT_PATH", "reports/html")
    
    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"