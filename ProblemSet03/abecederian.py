# Write a function called is_abecedarian that returns True if the letters in a word appear
# in alphabetical order (double letters are ok). How many abecedarian words are there? (i.e)
# "Abhor" or "Aux" or "Aadil" should return "True" Banana should return "False"

def abecedarian(list1):
    print(list1)
    for word in list1:
         if list(word)==sorted(word):
                print(word)

list1=[]
list1=input("Enter a string : ").split(" ")
abecedarian(list1)