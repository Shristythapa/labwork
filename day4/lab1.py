#Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else
#print ‘COMMON YEAR’.Hint: • a year is a leap year if its number is exactly divisible by 4 and is not
#exactly divisible by 100• a year is always a leap year if its number is exactly divisible by 400
a= int(input("enter a year"))
if a%4==0:
    print ("it is leap year")
else:
    print("it is not a leap year")