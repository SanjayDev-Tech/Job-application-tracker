from typing import List, Optional
from models import JobApplication
from storage import StorageManager

class JobTracker:
    """
    Main controller for managing job applications.
    """
    def __init__(self, storage_file: str = "data/applications.json"):
        self.storage = StorageManager(storage_file)
        self.applications: List[JobApplication] = self._load_applications()

    def _load_applications(self) -> List[JobApplication]:
        """
        Loads applications from storage and converts them to JobApplication objects.
        """
        data = self.storage.load()
        return [JobApplication.from_dict(item) for item in data]

    def _save_applications(self) -> None:
        """
        Serializes applications and saves to storage.
        """
        data = [app.to_dict() for app in self.applications]
        self.storage.save(data)

    def add_application(self, company: str, position: str, notes: str = "") -> JobApplication:
        """
        Adds a new job application.
        """
        new_app = JobApplication(company=company, position=position, notes=notes)
        self.applications.append(new_app)
        self._save_applications()
        return new_app

    def update_application_status(self, app_id: str, new_status: str) -> bool:
        """
        Updates the status of an existing application.
        """
        for app in self.applications:
            if app.id == app_id:
                app.update_status(new_status)
                self._save_applications()
                return True
        return False

    def delete_application(self, app_id: str) -> bool:
        """
        Deletes an application by ID.
        """
        initial_count = len(self.applications)
        self.applications = [app for app in self.applications if app.id != app_id]
        if len(self.applications) < initial_count:
            self._save_applications()
            return True
        return False

    def get_all_applications(self) -> List[JobApplication]:
        """
        Returns all applications.
        """
        return self.applications

    def search_applications(self, query: str, by_status: bool = False) -> List[JobApplication]:
        """
        Searches applications by company or status.
        """
        query = query.lower()
        if by_status:
            return [app for app in self.applications if query in app.status.lower()]
        return [app for app in self.applications if query in app.company.lower() or query in app.position.lower()]

    def get_application_by_id(self, app_id: str) -> Optional[JobApplication]:
        """
        Retrieves a single application by its ID.
        """
        for app in self.applications:
            if app.id == app_id:
                return app
        return None
