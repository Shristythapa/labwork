#you live 4 miles from the university. The bus drives to 25 mph but spends 2 minutes at each of the 10 stops on the way. How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph; then run the next two before jogging the last at 7mph before jogging th elast at 7mph again will this be quicker or slower
a=int((25//60)*4+2*10)
print(f"the bus journey will take {a} minutes.")
x=((1//7)*60)
y=((2//15)*60)
z=((1//7)*60)
b=x+y+z

print(f"if you jog and run then it will take {b} minutes")
if a>b:
    print("the bus will be quicker")
elif b>a:
    print("the jog and running will be quicker")
else:
    print("both will take the same amount of time")



