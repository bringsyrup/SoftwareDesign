#! /bin/env python
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""

def get_primes(n):
    """ Returns a list of all prime integers in the range [1,n] """
    return_val = []

    for i in range(1,n+1):
        isPrime = True
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
        if isPrime:
            return_val.append(i)
    return return_val


if __name__ == '__main__':
    print get_primes(7)