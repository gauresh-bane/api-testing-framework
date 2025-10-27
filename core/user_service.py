# User service for managing user operations

from core.api_client import APIClient
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class UserService:
    """Service layer for User API operations"""
    
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
    
    def create_user(self, user_data: Dict):
        """Create a new user"""
        logger.info(f"Creating user: {user_data.get('name')}")
        return self.api_client.post("/users/", data=user_data)
    
    def get_user(self, user_id: int):
        """Get user by ID"""
        logger.info(f"Getting user with ID: {user_id}")
        return self.api_client.get(f"/users/{user_id}")
    
    def get_all_users(self):
        """Get all users"""
        logger.info("Getting all users")
        return self.api_client.get("/users/")
    
    def update_user(self, user_id: int, update_data: Dict):
        """Update user information"""
        logger.info(f"Updating user ID: {user_id}")
        return self.api_client.put(f"/users/{user_id}", data=update_data)
    
    def delete_user(self, user_id: int):
        """Delete a user"""
        logger.info(f"Deleting user ID: {user_id}")
        return self.api_client.delete(f"/users/{user_id}")