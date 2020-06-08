def binaryToDecimal(n):
    temp=n
    decimal, i=0,0
    while temp!=0:
        rem=temp%10
        decimal=decimal+rem*pow(2,i)
        temp=temp//10
        i+=1
    return decimal
num = int(input("enter a binary number to find decimal equivalent: "))
print("the decimal equivalent of ",num," is: ",binaryToDecimal(num))