#Given three integers, print the smallest one. (Three integers should be user input) 
a=int(input("first num"))
b=int(input("second num"))
c=int(input("third num"))
if a>b and b>c:
    print(f"{a} is the greatest")
if b>c and c>a:
    print(f"{b} is greatest")
if c>b and b>a:
    print(f"{c} is the greatest")