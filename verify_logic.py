import os
import sys

# Ensure we can import the modules
sys.path.append(os.getcwd())

from tracker import JobTracker
from analytics import AnalyticsEngine
from reminders import ReminderEngine

def test_tracker():
    print("Starting verification test...")
    test_db = "data/test_applications.json"
    if os.path.exists(test_db):
        os.remove(test_db)
    
    tracker = JobTracker(storage_file=test_db)
    
    # 1. Test Adding
    print("Testing: Adding applications...")
    tracker.add_application("Google", "Software Engineer")
    tracker.add_application("Meta", "AI Researcher", "Followed up on 2026-02-10")
    tracker.add_application("Apple", "Product Manager")
    
    apps = tracker.get_all_applications()
    assert len(apps) == 3
    print("[OK] Add test passed.")

    # 2. Test Update
    print("Testing: Updating status...")
    app_id = apps[0].id
    tracker.update_application_status(app_id, "Interview")
    updated_app = tracker.get_application_by_id(app_id)
    assert updated_app.status == "Interview"
    print("[OK] Update test passed.")

    # 3. Test Analytics
    print("Testing: Analytics...")
    report = AnalyticsEngine.get_summary_report(apps)
    assert report['total_applications'] == 3
    assert report['status_distribution']['Interview'] == 1
    print("[OK] Analytics test passed.")

    # 4. Test Reminders
    print("Testing: Reminders...")
    # Apple application should trigger a reminder if we simulate it being old
    # Let's manually backdate it for testing
    apple_app = [a for a in apps if a.company == "Apple"][0]
    apple_app.last_updated = "2026-02-01 10:00:00" 
    
    reminder_engine = ReminderEngine(follow_up_threshold_days=7)
    pending = reminder_engine.get_pending_follow_ups(apps)
    assert len(pending) >= 1
    print("[OK] Reminder test passed.")

    # 5. Clean up
    if os.path.exists(test_db):
        os.remove(test_db)
    print("\nAll core logic tests passed successfully!")

if __name__ == "__main__":
    test_tracker()
