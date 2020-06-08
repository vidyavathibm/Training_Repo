def factR(n):
    if n==0:
        return 1
    else:
        return(n*factR(n-1))

num=int(input("enter a number to find factorial: "))
if num<0:
    print("Invalid number")
else:
    print("Factorial of a number: ",factR(num))