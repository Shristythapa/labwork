#given the integer N- the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24 hrs digital colock
N = int(input("enter the number of minutes passed since midnight"))
hours= N/60
minute = N%60
print(f"The time passed is {hours} hours and {minute} minutes. ")
