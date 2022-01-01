#3.	Write a Python program to count the number of strings where the string length is 2 or more and
#  the first and last character are same from a given list of strings
#Sample: list1 = [‘aba’,’121’,’kgf’,’abc’] 
list=["aba","121","kgf","abc"]
a=0
b=0
for i in list:
    if i[0]==i[-1]:
        a+=1
    elif len(i) >2:
        b+=1
print(f"There are {a} string with same first and last character.")
print(f"the number of string with more than 2 character are {b}")