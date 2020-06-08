# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.


def is_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        if sorted(str1.lower())!=sorted(str2.lower()):
            return False
        else:
            return True

str1=input("Enter the first string : ")
str2=input("Enter the second sting : ")
anagram_check=is_anagram(str1,str2)
if anagram_check:
    print("Anagram")
else:
    print("not an Anagram")