# Assertion utilities for test validation

from typing import Any, Dict
import logging

logger = logging.getLogger(__name__)

class AssertionHelper:
    """Helper class for common API test assertions"""
    
    @staticmethod
    def assert_status_code(actual: int, expected: int):
        """Assert HTTP status code"""
        logger.info(f"Asserting status code: expected={expected}, actual={actual}")
        assert actual == expected, f"Expected status {expected}, got {actual}"
    
    @staticmethod
    def assert_json_value(response_json: Dict, key: str, expected_value: Any):
        """Assert specific JSON value in response"""
        logger.info(f"Asserting JSON value: key={key}, expected={expected_value}")
        actual_value = response_json.get(key)
        assert actual_value == expected_value, f"Expected {key}={expected_value}, got {actual_value}"
    
    @staticmethod
    def assert_key_exists(response_json: Dict, key: str):
        """Assert that a key exists in JSON response"""
        logger.info(f"Asserting key exists: {key}")
        assert key in response_json, f"Key '{key}' not found in response"
    
    @staticmethod
    def assert_key_not_exists(response_json: Dict, key: str):
        """Assert that a key does not exist in JSON response"""
        logger.info(f"Asserting key does not exist: {key}")
        assert key not in response_json, f"Key '{key}' should not be in response"
    
    @staticmethod
    def assert_response_time(actual: float, max_time: float):
        """Assert response time is within acceptable range"""
        logger.info(f"Asserting response time: actual={actual}s, max={max_time}s")
        assert actual <= max_time, f"Response time {actual}s exceeded maximum {max_time}s"