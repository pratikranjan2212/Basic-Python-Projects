import string
import random

def PassGen():
    passlen = int(input("Enter the length of the password: \n"))
    s=[]  #Empty list to store the characters
    
    #Adding the characters to the list
    r1=string.ascii_lowercase
    r2=string.ascii_uppercase
    r3=string.digits
    r4=string.punctuation

    s.extend(list(r1))
    s.extend(list(r2))
    s.extend(list(r3))
    s.extend(list(r4))

    #Shuffling the characters
    random.shuffle(s)

    #Printing the password
    print("Your password is: ")
    print("".join(random.sample(s,passlen)))
    #print("".join(s[0:passlen])) Alternative way to print the password

PassGen()

