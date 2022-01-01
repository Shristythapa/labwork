# WAP which accepts marks of four subjects and display total marks, percentage and 
#grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, 
#less than 40% –> fail
a=int(input("enter the marks of first subject: "))
b=int(input("enter he marks of second subject: "))
c=int(input("enter the marks of third subject: "))
d=int(input("enter the marks of fourth subject: "))
s=a+b+c+d//4
print(f"you scored {s}",end=" ")
if s>70:
    print("distinction")
elif s>60:
    print("fist div")
elif s>40:
    print("pass")
else:
    print("fail")