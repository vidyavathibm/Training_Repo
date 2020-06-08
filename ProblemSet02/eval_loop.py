import math
def eval_loop():
    while(True):
        a=input("Enter the expression to evaluate :")
        if a!='done':
            res=eval(a)
        else:
            print("Last evaluated Result :",res)
            break;
eval_loop()


