#Write a Python program to sum three given integers. However, if two or more values areequal sum will be zero.
a=int(input("enter first integer"))
b=int(input("enter second integer"))
c=int(input("enter third integer"))
if a==b or b==c or c==a or a==b==c:
    print ("zero")
else:
    d=a+b+c
    print(f"{d} is the sum")