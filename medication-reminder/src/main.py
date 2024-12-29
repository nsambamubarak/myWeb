import schedule
import time
from schedule import medication_reminder

def main():
    print("Starting the medication reminder system...")
    
    # Schedule the reminders
    schedule.every().day.at("09:00").do(medication_reminder)
    schedule.every().day.at("13:00").do(medication_reminder)
    schedule.every().day.at("18:00").do(medication_reminder)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()