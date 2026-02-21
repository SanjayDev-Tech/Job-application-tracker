from typing import List
from datetime import datetime
from models import JobApplication

class ReminderEngine:
    """
    Detects applications that need follow-ups.
    """
    def __init__(self, follow_up_threshold_days: int = 7):
        self.threshold = follow_up_threshold_days

    def get_pending_follow_ups(self, applications: List[JobApplication]) -> List[JobApplication]:
        """
        Returns applications with 'Applied' status older than threshold days
        and no follow-up noted in the notes.
        """
        pending = []
        now = datetime.now()
        
        for app in applications:
            if app.status.lower() == "applied":
                try:
                    # Parse last_updated or date_applied
                    # We use last_updated to see when the last activity happened
                    # Format: 2026-02-17 14:38:19
                    dt_str = app.last_updated.split(' ')[0] # Get only the date part
                    last_act_date = datetime.strptime(dt_str, "%Y-%m-%d")
                    
                    days_since = (now - last_act_date).days
                    
                    if days_since >= self.threshold:
                        # Check if "Followed up" is already in notes to avoid duplicate reminders
                        if "Followed up" not in app.notes:
                            pending.append(app)
                except (ValueError, IndexError):
                    continue
        return pending

    def suggest_follow_up(self, app: JobApplication) -> str:
        """
        Generates a follow-up reminder message.
        """
        return f"Reminder: It's been {self.threshold}+ days since you applied to {app.company} for {app.position}. Consider sending a follow-up email."

    def mark_follow_up_done(self, app: JobApplication) -> None:
        """
        Updates application notes to indicate a follow-up was completed.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d")
        if app.notes:
            app.notes += f"\n- Followed up on {timestamp}"
        else:
            app.notes = f"- Followed up on {timestamp}"
        app.update_status(app.status) # Update last_updated timestamp
