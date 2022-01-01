#14.	Write a Python script to check if a given key already exists in a dictionary. 
data={1:"a",2:"b",3:"c",4:"d",5:"e"}
a=input("enter a key number")
if a in data:
    print("the key exist")
else:
    print("the key doesnt exist")