# Write a function named using_only() that takes a word and a string of letters, and that returns True
# if the word contains only letters in the list.
# Can you make a sentence using only the letters acefhlo? Other than "Hoe alfalfa?

def using_only(word,list1):
    for i in list1:
        if i not in word:
            return False
    return True

word=input("Enter a word: ")
list1=[]
list1=input("enter a string of letters: ").split(" ")
check=using_only(word,list1)
if check:
    print(word,"contains all the letters in the list")
else:
    print(word, "not contains all the letters in the list")