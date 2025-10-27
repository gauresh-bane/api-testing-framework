# Core utilities for API testing

from typing import Dict, Any, Optional
import requests
import json
import logging

logger = logging.getLogger(__name__)

class APIClient:
    """Base API client for making HTTP requests"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })
    
    def get(self, endpoint: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Perform GET request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET t{url}")
        response = self.session.get(url, params=params, headers=headers)
        logger.info(f"Response: {response.status_code}")
        return response
    
    def post(self, endpoint: str, data: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Perform POST request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST t{url}")
        response = self.session.post(url, json=data, headers=headers)
        logger.info(f"Response: {response.status_code}")
        return response
    
    def put(self, endpoint: str, data: Optional[Dict] = None, headers: Optional[Dict] = None) -> requests.Response:
        """Perform PUT request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        response = self.session.put(url, json=data, headers=headers)
        logger.info(f"Response: {response.status_code}")
        return response
    
    def delete(self, endpoint: str, headers: Optional[Dict] = None) -> requests.Response:
        """Perform DELETE request"""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url, headers=headers)
        logger.info(f"Response: {response.status_code}")
        return response