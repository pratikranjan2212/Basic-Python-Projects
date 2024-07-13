# This script is used to rename all the files in a folder to a number. This is useful when you have a cluttered folder and you want to rename all the files to a number.

import os

files = os.listdir("clutteredFolder")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
    i = i + 1