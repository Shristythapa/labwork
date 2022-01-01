#. Write a program function to find max of three numbers.(no parameter and no return type)
def max():
    a=int(input("first number"))
    b=int(input("second number"))
    c=int(input("third number"))
    if a>b and b>c:
        print(f"{a} is greatest")
    elif b>c and c>a:
        print(f"{b} is greatest")
    elif c>b and b>a:
        print(f"{c} is greatest")
max()
