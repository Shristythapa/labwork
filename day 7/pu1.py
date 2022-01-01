#Write a Python program to multiplies all the items in a list. 
a=list(map(int,input("enter the values of list")))
print(f"{a} is your entered list.")
b=1
c=1
for i in a:
    c=i*b
    b=c
print(b)