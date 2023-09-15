import time
import plyer

def reminder():

    # Display message
    title = "Drink Water Reminder"
    message = "Rohan, its time to drink some water....Stay hydrated"
    # generation of notification
    plyer.notification.notify(
        title = title,
        message = message,
        app_name = "P10 - Drink Water Reminder",
        timeout = 5  # notification display time
    )

def main():

    interval = 1800  # the reminder will be after every 30 mins
    while True:
        reminder()
        time.sleep(interval)

if __name__ == "__main__":
    main()