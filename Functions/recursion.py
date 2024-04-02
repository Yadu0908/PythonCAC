# recursion concept through factorial concept.

def factorial(num):

    if(num == 0):

        return 1

    else:

        return num * factorial(num-1)   # function is called inside the function.

print(factorial(5))