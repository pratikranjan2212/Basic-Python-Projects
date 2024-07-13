import string
import random

# Ask the user for the message
sms = input("Enter your message: ")
words = sms.split(" ")

# Ask the user whether they want to code or decode
coding = input("Enter 1 for Coding and 0 for Decoding: ")
coding = True if (coding=="1") else False

# Check if the user wants to code or decode
if coding:
    newwords = []
    for word in words:
        if len(word) >= 3:
            s1 = ""
            s2 = ""
            r1 = random.choices(string.ascii_lowercase, k=3)
            r2 = random.choices(string.ascii_lowercase, k=3)
            for i in r1:
                s1 += i
            for j in r2:
                s2 += j
            newsms = s1 + word[1:] + word[0] + s2
            newwords.append(newsms)
        else:
            newwords.append(word[::-1])

    print("Your new message is: ")
    print(" ".join(newwords))

else:
    newwords = []
    for word in words:
        if len(word) >= 3:
            newsms = word[3:-3]
            newsms = newsms[-1] + newsms[:-1]
            newwords.append(newsms)
        else:
            newwords.append(word[::-1])

    print("Your new message is: ")
    print(" ".join(newwords))


