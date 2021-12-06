#A student will not be allowed to sit in exam if his/her attendance is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.And print percentage of class attendedIs student is allowed to sit in exam or not.
a=int(input("enter the number of class heald"))
b=int(input("number of class attended"))
c=(b/a)*100
print(f"{c}% of class is attended")
if c<75:
    print ("you are not allowed to sit in exam")
if c>=75:
    print("you are allowed to sit in exam")
