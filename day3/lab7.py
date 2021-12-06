#Given a positive real number, print its fractional part. 
a=float(input("enter a number"))
import math
b=math.modf(a)
print(b)