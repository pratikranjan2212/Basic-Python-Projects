# This is a python script that gives shoutout to the people in the list.

import pyttsx3
engine=pyttsx3.init()

l = ["Elon", "Tim", "Mark"]

for i in range(0,len(l)+1):
  engine.say(f"Shoutout to {l[i]}")
  engine.runAndWait()
  if i==len(l)-1:
    break