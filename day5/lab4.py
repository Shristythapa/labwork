#4. Write a Python program to construct the following pattern, using a nested for loop.
#* 
#* *
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* *
for i in range(0,5):
    for j in range(0,i):
        print("*",end=" ")
    print("*")
for i in range(4,0,-1):
    for j in range(i-1):
        print("*",end=" ")
    print("*")