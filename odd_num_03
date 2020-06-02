#1) Write a program that examines three variables—x, y, and z— and prints the largest odd number among them.
# If none of them are odd, it should print a message to that effect.
def odd_check(num):
    return not(num%2 == 0)

def number(x, y, z):
    l = [e for e in [x, y, z] if odd_check(e)]
    try:
        print(max(l))
    except ValueError:
        print("None of them are odd")
number(11,20,30)
