#Write a Python program to guess a number between 1 to 9.
import random
a= random.randrange(1,10)

i=1
while i>=1:
    b=int(input("enter a number between 1 and 9"))
    if a==b:
        print("well gussed")
    i+=1

