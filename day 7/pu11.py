#11.	Write a Python program to remove an item from a set if it is present in the set. 
a={"a","h","b","g","c","f","d","e"}
b=input("enter a character")
if b in a:
    a.discard(b)
    print(a)
else:
    print(a)
