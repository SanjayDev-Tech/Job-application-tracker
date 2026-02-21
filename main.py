import sys
import os
from tracker import JobTracker
from analytics import AnalyticsEngine
from reminders import ReminderEngine

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print("\n" + "="*50)
    print(f"{title:^50}")
    print("="*50)

def main():
    tracker = JobTracker()
    reminder_engine = ReminderEngine(follow_up_threshold_days=7)
    
    while True:
        # Check for reminders at start of each loop
        pending = reminder_engine.get_pending_follow_ups(tracker.get_all_applications())
        
        print_header("JOB APPLICATION TRACKER")
        if pending:
            print(f"🔔 NOTIFICATION: You have {len(pending)} pending follow-ups!")
            print("-" * 50)

        print("1. Add New Application")
        print("2. View All Applications")
        print("3. Update Application Status")
        print("4. Delete Application")
        print("5. Search Applications")
        print("6. View Analytics")
        print("7. Manage Reminders/Follow-ups")
        print("8. Exit")
        
        choice = input("\nSelect an option (1-8): ").strip()

        if choice == '1':
            company = input("Company Name: ").strip()
            position = input("Position: ").strip()
            notes = input("Notes (optional): ").strip()
            if company and position:
                app = tracker.add_application(company, position, notes)
                print(f"\n✅ Added application for {app.position} at {app.company} (ID: {app.id})")
            else:
                print("\n❌ Company and Position are required.")

        elif choice == '2':
            apps = tracker.get_all_applications()
            if not apps:
                print("\nNo applications found.")
            else:
                print_header("ALL APPLICATIONS")
                print(f"{'ID':<10} {'Company':<20} {'Position':<20} {'Status':<15}")
                print("-" * 65)
                for app in apps:
                    print(f"{app.id:<10} {app.company[:19]:<20} {app.position[:19]:<20} {app.status:<15}")

        elif choice == '3':
            app_id = input("Enter Application ID to update: ").strip()
            print("Statuses: Applied, OA, Interview, Offer, Rejected")
            new_status = input("Enter New Status: ").strip()
            if tracker.update_application_status(app_id, new_status):
                print(f"\n✅ Status updated to {new_status}")
            else:
                print(f"\n❌ Application ID {app_id} not found.")

        elif choice == '4':
            app_id = input("Enter Application ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete {app_id}? (y/n): ").lower()
            if confirm == 'y':
                if tracker.delete_application(app_id):
                    print(f"\n✅ Deleted application {app_id}")
                else:
                    print(f"\n❌ Application ID {app_id} not found.")

        elif choice == '5':
            query = input("Search by Company or Status: ").strip()
            search_apps = tracker.search_applications(query)
            if not search_apps:
                # Try search by status if company search yields nothing
                search_apps = tracker.search_applications(query, by_status=True)
            
            if not search_apps:
                print(f"\nNo results found for '{query}'")
            else:
                print_header(f"SEARCH RESULTS: {query}")
                for app in search_apps:
                    print(f"[{app.id}] {app.company} - {app.position} ({app.status})")

        elif choice == '6':
            report = AnalyticsEngine.get_summary_report(tracker.get_all_applications())
            print_header("ANALYTICS SUMMARY")
            print(f"Total Applications: {report['total_applications']}")
            print(f"Applications in last 7 days: {report['recent_activity']}")
            print(f"Success Rate (Offers): {report['success_rate']}")
            print("\nStatus Distribution:")
            for status, count in report['status_distribution'].items():
                print(f" - {status}: {count}")

        elif choice == '7':
            pending = reminder_engine.get_pending_follow_ups(tracker.get_all_applications())
            if not pending:
                print("\nNo pending follow-ups required at this moment.")
            else:
                print_header("PENDING FOLLOW-UPS")
                for i, app in enumerate(pending, 1):
                    print(f"{i}. {app.company} ({app.position}) - Applied on {app.date_applied}")
                
                sub_choice = input("\nMark one as completed? (Enter number or 'n' to go back): ").strip()
                if sub_choice.isdigit():
                    idx = int(sub_choice) - 1
                    if 0 <= idx < len(pending):
                        reminder_engine.mark_follow_up_done(pending[idx])
                        tracker._save_applications() # Persist the note change
                        print(f"\n✅ Marked follow-up for {pending[idx].company} as completed.")
                    else:
                        print("\n❌ Invalid number.")

        elif choice == '8':
            print("\nGoodbye!")
            sys.exit()

        else:
            print("\n❌ Invalid choice. Please try again.")

        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()
