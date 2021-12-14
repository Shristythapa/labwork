#Write a Python program that accepts a string and calculate the number of digits and letters
a=input("enter a string")
d=c=0
for i in a:
    if i.isdigit():
        d=d+1
    if i.isalpha():
        c=c+1
print(f"Number of digits is {d}")
print(f"Numbers of letters is {c}")