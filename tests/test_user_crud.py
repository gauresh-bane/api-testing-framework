# Test cases for User CRUD operations

import pytest
from core.assertions import AssertionHelper
import logging

logger = logging.getLogger(__name__)

@pytest.mark.smoke
class TestUserCRUD:
    """Test suite for User CRUD operations"""
    
    def test_create_user_success(self, user_service, test_data):
        """Test successful user creation"""
        logger.info("Testing user creation")
        user_data = test_data["valid_users"][0]
        
        response = user_service.create_user(user_data)
        
        AssertionHelper.assert_status_code(response.status_code, 200)
        response_json = response.json()
        AssertionHelper.assert_key_exists(response_json, "id")
        AssertionHelper.assert_json_value(response_json, "name", user_data["name"])
        AssertionHelper.assert_json_value(response_json, "email", user_data["email"])
    
    def test_get_user_success(self, user_service, test_data):
        """Test getting a user by ID"""
        logger.info("Testing get user")
        
        # First create a user
        user_data = test_data["valid_users"][1]
        create_response = user_service.create_user(user_data)
        user_id = create_response.json()["id"]
        
        # Get the user
        response = user_service.get_user(user_id)
        
        AssertionHelper.assert_status_code(response.status_code, 200)
        response_json = response.json()
        AssertionHelper.assert_json_value(response_json, "id", user_id)
    
    def test_update_user_success(self, user_service, test_data):
        """Test updating a user"""
        logger.info("Testing user update")
        
        # Create a user
        user_data = test_data["valid_users"][2]
        create_response = user_service.create_user(user_data)
        user_id = create_response.json()["id"]
        
        # Update the user
        update_data = {"name": "Updated Name"}
        response = user_service.update_user(user_id, update_data)
        
        AssertionHelper.assert_status_code(response.status_code, 200)
        response_json = response.json()
        AssertionHelper.assert_json_value(response_json, "name", "Updated Name")
    
    def test_delete_user_success(self, user_service, test_data):
        """Test deleting a user"""
        logger.info("Testing user deletion")
        
        # Create a user
        user_data = test_data["valid_users"][0]
        user_data["email"] = "delete@example.com"  # Unique email
        create_response = user_service.create_user(user_data)
        user_id = create_response.json()["id"]
        
        # Delete the user
        response = user_service.delete_user(user_id)
        
        AssertionHelper.assert_status_code(response.status_code, 200)
        
        # Verify user no longer exists
        get_response = user_service.get_user(user_id)
        AssertionHelper.assert_status_code(get_response.status_code, 404)