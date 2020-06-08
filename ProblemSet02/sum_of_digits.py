def sum_of_digits(str):
    sum=0
    for i in str:
        if i.isdigit():
            sum=sum+int(i)
    print("Sum of digits in ",str,"is",sum)

string=input("enter a string : ")
sum_of_digits(string)
