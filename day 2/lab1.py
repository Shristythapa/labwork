#convert second to day, hours ,minutes and seconds
s= 86400
min=s/60
print(f"{s} seconds is {min} minutes")

hours=min/60
print(f"{min} minutes is {hours} hours")

days=hours/24
print(f"{hours} hours is {days} days")

s=int(input("enter the value of second"))
d=(((s/60)/60)/24)
print(f"{s} seconds is {d} days")
