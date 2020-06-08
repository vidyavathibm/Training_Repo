# A number, a, is a power of b if it is divisible by b and a/b is a power of b.
# Write a function called is_power that takes parameters a and b and returns True
# if a is a power of b. Note: you will have to think about the base case.


def is_power(a,b):
    c = a/b
    if ((a%b == 0) and (c%b == 0)):
        return True
    else:
        return False


a=int(input("enter first number: "))
b=int(input("enter second number: "))
if(is_power(a,b)):
    print(a," is power of ",b)
else:
    print(a, " is not power of ", b)