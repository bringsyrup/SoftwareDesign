#! /bin/env python

'''all the things'''

from math import factorial as fact

def factorial(n):
    if type(n) != int:
        print "need an integer for factrialization to occur"
        return None
    else:
        return fact(n)

def is_prime(n):
    if type(n) != int:
        print "need an integer to check for prime"
        return None
    else:
        if n % (i for i in range(2,n)) == 0 and n != 2:
            return False
        else:
            return True

def sum_integers(x, y):
    rnge = range(x, y)
    cumsum = 0
    for item in rnge:
        cumsum += item
    return cumsum
