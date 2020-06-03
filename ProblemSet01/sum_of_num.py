# 6)Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'.
# Write a program that prints the sum of the numbers in s.


sum=0
s = '1.23,2.4,3.123'
list1=s.split(',')
print(list1)
for i in list1:
    sum=sum+float(i)
print(sum)
