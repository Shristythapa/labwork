#Write a program function to find min of three numbers.(no parameter and no return type)
def min():
    a=int(input("first num"))
    b=int(input("second num"))
    c=int(input("third num"))
    if a<b and b<c:
        print(f"{a} is min")
    elif b<c and c<a:
        print(f"{b} is min")
    elif c<a and a<b:
        print(f"{c} is min")
min()