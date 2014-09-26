#! /bin/env python

from random import random

def random_float(rnge):
    return random()*(rnge[-1]-rnge[0])

if __name__=="__main__":
    print random_float([1,9])


