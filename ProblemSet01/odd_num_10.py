
#3) Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.
#

def odd_check(num):
    return not(num%2 == 0)
list1=[]
for i in range(10):
    list1.append(int(input()))

l = [e for e in list1 if odd_check(e)]
try:
    print(max(l))
except ValueError:
    print("None of them are odd")

##########################################
list1 = []
for i in range(10):
    list1.append(int(input()))

l = [e for e in list1 if e % 2 != 0]
try:
    print(max(l))
except ValueError:
    print("None of them are odd")
