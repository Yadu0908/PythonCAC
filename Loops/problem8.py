# Checking for a number is it prime number or not. (You can use other kind of logics too)

num = 11
is_prime = True

if(num > 1):

    for i in range (2, int(num ** 0.5) + 1):

        if(num% i == 0):

            is_prime = False
            break

    if(is_prime):

        print("Prime number");

    else:

        print("Not a prime number")

#! Prime number's are the number which are the multiple of 1 and its own.