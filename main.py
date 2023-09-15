import time
import plyer

def message_generation(hour):
    if (hour >= 3 and hour < 12):
        message = "Good Morning Rohan, its time to drink some water....Stay hydrated"
    elif (hour >= 12 and hour < 18):
        message = "Good Afternoon Rohan, its time to drink some water....Stay hydrated"
    elif (hour >= 18 and hour < 21):
        message = "Good Evening Rohan, its time to drink some water....Stay hydrated"
    elif (hour >= 21 and hour <= 24):
        message = "Rohan, its time to drink some water....Stay hydrated Good Night"
    elif (hour >= 0 and hour < 3):
        message = "Rohan, its time to drink some water....Stay hydrated Good Night"
    return message

def reminder():

    # display salutation
    hour = int(time.strftime('%H'))

    # Display details
    title = "Drink Water Reminder"
    message = message_generation(hour)


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