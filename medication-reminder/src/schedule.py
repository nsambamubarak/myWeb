import schedule
import time

def medication_reminder():
    print("Time to take your medication!")

# Schedule the reminder for specific times
schedule.every().day.at("09:00").do(medication_reminder)
schedule.every().day.at("13:00").do(medication_reminder)
schedule.every().day.at("18:00").do(medication_reminder)

while True:
    schedule.run_pending()
    time.sleep(1)