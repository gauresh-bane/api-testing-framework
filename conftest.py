# Pytest configuration and fixtures

import pytest
from core.api_client import APIClient
from core.user_service import UserService
from config.settings import Config
from utils.logger import setup_logger
from utils.data_loader import DataLoader
import logging

# Setup logger
logger = setup_logger(__name__)

@pytest.fixture(scope="session")
def api_client():
    """Create API client for all tests"""
    logger.info(f"Initializing API client with base URL: {Config.API_BASE_URL}")
    return APIClient(Config.API_BASE_URL)

@pytest.fixture(scope="session")
def user_service(api_client):
    """Create User service for all tests"""
    logger.info("Initializing User service")
    return UserService(api_client)

@pytest.fixture(scope="session")
def test_data():
    """Load test data from JSON file"""
    logger.info(f"Loading test data from: {Config.TEST_DATA_PATH}")
    return DataLoader.load_json(Config.TEST_DATA_PATH)

@pytest.fixture(autouse=True)
def log_test_info(request):
    """Log test information before and after each test"""
    logger.info(f"\n===== Starting Test: {request.node.name} =====")
    yield
    logger.info(f"\n===== Finished Test: {request.node.name} =====")