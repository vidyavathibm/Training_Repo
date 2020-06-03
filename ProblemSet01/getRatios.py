
# Implement a function that satisfies the specification. Use a try-except block.
#
# def getRatios(vect1, vect2):
# 	"""Assumes: vect1 and vect2 are lists of equal length of numbers
# 	Returns: a list containing the meaningful values of
# 	vect1[i]/vect2[i]"""

# def getRatios(vect1,vect2):
#     if len(vect1)==len(vect2):
#         for i in range(len(vect1)):
#             print(int(vect1[i])/int(vect2[i]))
#
# vect1=list(input(""))
# vect2=list(input(""))
# print(vect1)
# print(vect2)
# getRatios(vect1,vect2)

###############################################

try:
    def getRatios(vect1, vect2):
        if len(vect1) == len(vect2):
            for i in range(len(vect1)):
                print(int(vect1[i]) / int(vect2[i]))


    vect1 = list(input(""))
    vect2 = list(input(""))
    print(vect1)
    print(vect2)
    print(getRatios(vect1, vect2))


except ZeroDivisionError:
	print('ZeroDivisionError')
except:
	print('error occured')
else:
	print('ELSE BLOCK')
finally:
	print('FINALLY BLOCK')