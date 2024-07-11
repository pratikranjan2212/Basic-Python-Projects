import pyttsx3
import time

engine=pyttsx3.init()
def drink_water_reminder():
    while True:
        engine.say("Please drink water")
        engine.runAndWait()
        # Wait for one hour
        time.sleep(3600)  # 3600 seconds = 1 hour

# Call the function to start the reminder
drink_water_reminder()