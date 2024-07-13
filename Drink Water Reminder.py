import pyttsx3
from plyer import notification
import time

# Initialize the Text-to-Speech engine
engine=pyttsx3.init()

# Function to remind the user to drink water
def drink_water_reminder():
    while True:
        # Display a notification
        notification.notify(
            title = "Please Drink Water Now",
            message = "Drinking water is essential to keep your body hydrated and healthy. Please drink water now.",
            app_icon = "C:\\Users\\priti\\Downloads\\aqua.ico",
            timeout = 10 # The notification will be displayed for 10 seconds
        )
        engine.say("Please drink water")
        engine.runAndWait()
        # Wait for one hour
        time.sleep(3600)  # 3600 seconds = 1 hour

# Call the function to start the reminder
drink_water_reminder()