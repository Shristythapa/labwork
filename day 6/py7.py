#Write a Python program to multiply all the numbers in a list.
#Sample list = [8,2,3,-1,7]
a=[8,2,3,-1,7]
l=len(a)
d=0
e=1
for i in range(l):
    d=e*a[i]
    e=d
   
    
    
print(d)