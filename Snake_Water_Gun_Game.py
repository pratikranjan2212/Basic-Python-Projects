# This is a simple game of Snake, Water and Gun. The user has to choose between Snake, Water and Gun and the computer will also choose one of the three. 

import random

# Randomly choosing between Snake, Water and Gun
comp = random.randint(0, 2)
user = int(input("Enter 0 for Snake, 1 for water and 2 for Gun:\n"))

# Function to check the result
def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  return 1

score = check(comp, user)

# Added Result
print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")
  



