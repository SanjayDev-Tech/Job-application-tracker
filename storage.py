import json
import os
from typing import List, Dict, Any

class StorageManager:
    """
    Handles JSON file operations for persistence.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """
        Creates the data directory and file if they don't exist.
        """
        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        if not os.path.exists(self.file_path):
            self.save([])

    def load(self) -> List[Dict[str, Any]]:
        """
        Loads data from the JSON file.
        """
        try:
            if not os.path.exists(self.file_path):
                return []
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading storage: {e}")
            return []

    def save(self, data: List[Dict[str, Any]]) -> bool:
        """
        Saves data to the JSON file.
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            return True
        except IOError as e:
            print(f"Error saving storage: {e}")
            return False
