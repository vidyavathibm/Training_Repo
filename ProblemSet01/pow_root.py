# 5)Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that
# 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists
# , it should print a message to that effect.
n=int(input())

for i in range(1,6):
	root=n**(1/i)
	print('For ',i)

	if int(root)**i==n:
		print ("root=",root,"pow=",i)
	else:
		print('not found')