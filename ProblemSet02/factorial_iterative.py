def factI(n):
    fact=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact


num = int(input("enter a number to find factorial: "))
if num < 0:
    print("Invalid number")
else:
    print("Factorial of a number: ", factI(num))