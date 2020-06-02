# One way of computing square roots is Newton’s method. Suppose that you want to know the square root of a.
# If you start with almost any estimate, x, you can compute a better estimate with the following formula:
# y = (x + a/x)/2 For example, if a is 4 and x is 3:
# >>> a = 4.0
# >>> x = 3.0
# >>> y = (x + a/x) / 2
# >>> print y
# 2.16666666667
# a) Write a function NewtonSqrt() to abstract the Newton's Method of calculation Square roots.

def NewtonSqrt(a,x):
    y=(x + a / x) / 2
    return y

a=int(input("enter a number to find square root : "))
x=int(input("enter guess value of the square root : "))
print("Square root of",a,"using Newton's square root method :",NewtonSqrt(a,x))
