#WAP which accepts marks of four subjects and display total marks, percentage and grade.
#  Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
a=int(input("first subject"))
b=int(input("second subject"))
c=int(input("third subject"))
d=int(input("fourth subject"))
e=(a+b+c+d)/400*100
print(e)