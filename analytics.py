from typing import List, Dict, Any
from collections import Counter
from datetime import datetime, timedelta
from models import JobApplication

class AnalyticsEngine:
    """
    Computes statistics for job applications.
    """
    @staticmethod
    def get_total_count(applications: List[JobApplication]) -> int:
        return len(applications)

    @staticmethod
    def get_status_distribution(applications: List[JobApplication]) -> Dict[str, int]:
        """
        Counts applications by status.
        """
        status_counts = Counter(app.status for app in applications)
        return dict(status_counts)

    @staticmethod
    def get_success_rate(applications: List[JobApplication]) -> float:
        """
        Calculates (Offers / Total) ratio.
        """
        if not applications:
            return 0.0
        offers = sum(1 for app in applications if app.status.lower() == "offer")
        return (offers / len(applications)) * 100

    @staticmethod
    def get_applications_last_7_days(applications: List[JobApplication]) -> int:
        """
        Counts applications submitted in the last 7 days.
        """
        now = datetime.now()
        seven_days_ago = now - timedelta(days=7)
        count = 0
        for app in applications:
            try:
                app_date = datetime.strptime(app.date_applied, "%Y-%m-%d")
                if app_date >= seven_days_ago:
                    count += 1
            except ValueError:
                continue
        return count

    @staticmethod
    def get_summary_report(applications: List[JobApplication]) -> Dict[str, Any]:
        """
        Generates a comprehensive analytics summary.
        """
        return {
            "total_applications": AnalyticsEngine.get_total_count(applications),
            "status_distribution": AnalyticsEngine.get_status_distribution(applications),
            "success_rate": f"{AnalyticsEngine.get_success_rate(applications):.2f}%",
            "recent_activity": AnalyticsEngine.get_applications_last_7_days(applications)
        }
