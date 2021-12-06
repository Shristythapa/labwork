#Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".
a=int(input("enter your age"))
b=input("enter your gender")
if b=="female":
    print("you will work in urban area")
elif a>20 and a<40 and b=="male":
    print ("you may work anywhere")
elif a>40 and a<60 and b=="male":
    print("you may only work in urban area")
else:
    print("invalid")


