# Modify your program to prompt the user to enter a string of forbidden letters
# and then print the number of words that don’t contain any of them.
# Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

def avoids_forbidden():
    user_input = input("Enter a string of forbidden letters!")
    string = input("Enter string of words")
    word=""
    word=string.split(" ")
    count = 0
    for line in word:
        print(line)
        if user_input not in line:
            count = count + 1
    print(count)

avoids_forbidden()