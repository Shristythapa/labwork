#write a function called fizz_buzz that takes a number, If the number is divisible by 3 it should return "Fizz"
#if the number is divisible by 5, it should return "Buzz".IF THE number is divisible by both then it should return "FizzBuzz"
#otherwise it should return the same number.

def fizz_buzz(b,c,d):
    a=int(input("enter a number"))
    if a%3==0:
        return b
       
    elif a%5==0:
        return c
    elif a%5==0 and a%3==0:
        return d
    else:
        print(a)
     
    
ans=fizz_buzz("fizz","buzz","fizzbuzz")
print(ans)
