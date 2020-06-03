
# Write a function isIn() that accepts two strings as arguments and returns True if either string occurs anywhere
# in the other, and False otherwise. Hint: you might want to use the built-in str operation in.
def isIn(str1,str2):
    if str1 in str2:
        return True
    else:
        return False

string1=input("enter first string: ")
string2=input("enter second string: ")

print(isIn(string1,string2))