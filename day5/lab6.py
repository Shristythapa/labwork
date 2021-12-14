# Write a Python program to count the number of even and odd numbers from a series of numbers.
a=[12,3,4,5,63,7,4,86,8,6,434,36,87,56453,258,214,2,2465,342,56]
n=len(a)
b=[]
c=[]
for i in range(n):
    if a[i]%2==0:
       b.append(a[i])
       
    elif not a[i]%2==0:
        c.append(a[i])
print("the numbers of even number is",str(len(b)))
print("The numbers of odd number is", str(len(c)))
            

