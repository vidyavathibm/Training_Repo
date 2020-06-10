# Modify the above program to print only the words that have no “e” and compute the percentage of the words
# in the list have no “e.”

def has_no_e(l):
    cnt=0
    print("Words which are not having 'e' in the list")
    for i in l:
        if 'e' not in i:
           print (i)
           cnt+=1
    print("No. of words not having e  ",cnt)
    print(len(l))
    per=(cnt/len(l))*100
    print("percentage of the words in the given list have no 'e' ","%.f"%per+"%")
list1=[]
list1=input("Enter the list of words : ").split(" ")
has_no_e(list1)