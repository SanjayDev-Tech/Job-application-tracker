import uuid
from datetime import datetime
from typing import Dict, Any

class JobApplication:
    """
    Represents a single job application.
    """
    def __init__(
        self, 
        company: str, 
        position: str, 
        status: str = "Applied", 
        id: str = None, 
        date_applied: str = None, 
        last_updated: str = None,
        notes: str = ""
    ):
        self.id = id if id else str(uuid.uuid4())[:8]
        self.company = company
        self.position = position
        self.status = status
        self.date_applied = date_applied if date_applied else datetime.now().strftime("%Y-%m-%d")
        self.last_updated = last_updated if last_updated else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.notes = notes

    def update_status(self, new_status: str) -> None:
        """
        Updates the status of the application and the last updated timestamp.
        """
        self.status = new_status
        self.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the object to a dictionary for JSON serialization.
        """
        return {
            "id": self.id,
            "company": self.company,
            "position": self.position,
            "status": self.status,
            "date_applied": self.date_applied,
            "last_updated": self.last_updated,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'JobApplication':
        """
        Creates a JobApplication instance from a dictionary.
        """
        return cls(
            company=data["company"],
            position=data["position"],
            status=data["status"],
            id=data["id"],
            date_applied=data["date_applied"],
            last_updated=data.get("last_updated"),
            notes=data.get("notes", "")
        )

    def __repr__(self) -> str:
        return f"JobApplication(id={self.id}, company='{self.company}', status='{self.status}')"
