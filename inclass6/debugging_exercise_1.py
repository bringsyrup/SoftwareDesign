#! /bin/env python
"""
Created on Sun Feb  9 17:52:54 2014

@author: pruvolo
"""

import numpy as np

def cumulative_sum(L):
    """ returns a list where each element in the returned list is the
    	cumulative sum of the elements up to the corresponding element in
	the original list.
	
	L: the original list
	returns: a new list where element i is equal to the sum of element
		 0 through i in the original list """
    L = np.asarray(L)
    new = np.zeros(len(L))
    for i in range(len(L)):
        new[i] = new[i-1] + L[i]
    return new 

if __name__ == '__main__':
    print cumulative_sum([1, 2, 3])
