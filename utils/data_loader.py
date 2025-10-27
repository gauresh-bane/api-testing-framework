# Utilities for loading test data

import json
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class DataLoader:
    """Utility class for loading test data"""
    
    @staticmethod
    def load_json(file_path: str) -> Dict[str, Any]:
        """Load JSON data from file"""
        logger.info(f"Loading test data from: {file_path}")
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in file: {file_path} - {e}")
            raise