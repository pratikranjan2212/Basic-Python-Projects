import string
import random

sms = input("Enter your message: ")
words = sms.split(" ")

coding = input("Enter 1 for Coding and 0 for Decoding: ")
coding = True if (coding=="1") else False

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


# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

# st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))
  
  