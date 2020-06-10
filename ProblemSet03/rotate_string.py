# Write a function called rotate_word() that takes a string and
# # an integer as parameters, and that returns a new string that contains the letters
# # from the original string "rotated" by the given amount. For example, "cheer"
# # rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed". You might want to use the built-in
# # functions ord, which converts a character to a numeric code, and chr,
# # which converts numeric codes to characters.
#ord-takes character and gives its ascii
#chr-takes ascii and gives its corresponding char

def rotate_word(s,n):
    s1=""
    for i in s:
        s1=s1+chr(ord(i)+n)
    print("Rotated word : ",s1)

string=input("enter a string needs to be rotated : ")
num=int(input("Enter a number : "))
rotate_word(string,num)
