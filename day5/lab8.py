#Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it
num1=0
num2=1
for i in range(51):
    print(num1,end=" ")
    res=num1+num2
    num1=num2
    num2=res

    