#Write a Python program to convert temperatures to and from celsius, fahrenheit.
 #C = (5/9) * (F - 32)

f=int(input("enter fahrenheit"))
c=(5/9)*(f-32)
print(c)
c=int(input("enter celsius"))
f=(c-32)/1.8
print(f)
