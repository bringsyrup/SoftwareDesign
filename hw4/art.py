#! /bin/env python

'''
create some random art or something
'''

from random import randint
from math import pi
import re
import numpy as np
import Image as img

rand_func = []

def random_list(n):
    rand_list = []
    for i in range(n):
        rand_list.append(randint(0, n))
    return rand_list

def random_func(recurs):
    '''
    recursive function that produces a random function because as we all know the best art takes no thought at all. you think I'm kidding.
    '''
    options = ["x", "y", "np.sin", "np.cos", "pi"]
    rand_func.append(options[randint(0, len(options)-1)])
    if recurs == 0:
        func_str = "res = "
        operands = ["-", "+", "*"]
        paren_count = 0
        for i, opt in enumerate(rand_func):
            if func_str[-1] == ")":
                func_str += operands[randint(0, len(operands)-1)] + opt
            else:
                func_str += opt
            if i == len(rand_func)-1:
                if paren_count > 0:
                    if func_str[-3:] not in ["sin", "cos"]:
                        func_str += ")"*paren_count
                    else:
                        final = ["x", "y", "pi"]
                        func_str += "(" + final[randint(0, len(final)-1)] + ")"*(paren_count+1)
                else:
                    final = ["x", "y", "pi"]
                    func_str += "(" + final[randint(0, len(final)-1)] + ")"*(paren_count+1)
                final_count = len(re.findall('[(]', func_str)) - len(re.findall('[)]', func_str))
            elif i in random_list(i) and func_str[-3:] not in ["sin", "cos"] and paren_count > 0:
                func_str += ")"
                paren_count -= 1
            else:
                if paren_count > 0 and func_str[-3:] not in ["sin", "cos"]:
                        if i in random_list(i):
                            func_str += ")"
                            paren_count -= 1
                if opt in ["x", "y", "pi"]:
                    if opt != "pi":
                        if paren_count > 0:
                            if func_str[-1] == "(" or func_str[-4:-2] == "pi":
                                func_str += ")" + operands[randint(0, len(operands)-1)]
                                paren_count -= 1
                            else:
                                func_str += operands[randint(0, len(operands)-1)]
                        else: 
                            func_str += operands[randint(0, len(operands)-1)]
                    else:
                        func_str += operands[randint(0, len(operands)-1)]
                elif opt == "np.sin" or opt == "np.cos":
                    func_str += "("
                    paren_count += 1
        return func_str
    else:
        return random_func(recurs - 1)

def get_func(lower, upper):
    '''
    get_func function generated from random_func()
    '''
    func = random_func(randint(lower, upper))
    print func
    return func 

def evaluate(function, x, y):
    '''
    evaluate frunction from get_func when called from another source such as map_colors
    avoids generating a new function every time you want to execute, so you can call this function multiple times for the same random function
    '''
    exec function
    return res

def map_colors():
    '''
    map generated function/s to rgb colors and plot them in a png
    '''
    xaxis = np.linspace(-10, 10, 300)
    yaxis = np.linspace(-10, 10, 300)
    xg, yg = np.meshgrid(xaxis, yaxis)
    func0 = get_func(40, 65)
    res_grid0 = evaluate(func0, xg, yg)
    raw_min0 = np.min(res_grid0)
    raw_max0 = np.max(res_grid0)
    func1 = get_func(5, 30) #comment out ...
    res_grid1 = evaluate(func1, xg, yg) # ...
    raw_min1 = np.min(res_grid1) # ...
    raw_max1 = np.max(res_grid1) # ...
    func2 = get_func(75, 100) # ...
    res_grid2 = evaluate(func2, xg, yg) # ...
    raw_min2 = np.min(res_grid2) # ...
    raw_max2 = np.max(res_grid2) # ... for coloration based on one function
    color = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
            )
    new = img.new('RGB', (300, 300))
    new_img = new.load()
    for i in range(new.size[0]):
        for j in range(new.size[1]):
            x = i/15. - 10.
            y = j/15. - 10.
            print x
            res0 = evaluate(func0, x, y)
            res1 = evaluate(func1, x, y) #comment out for coloration based on one function
            res2 = evaluate(func2, x, y) #comment out for coloration based on one function
            color_remap = (
                    int(color[0]*(res0 - raw_min0)/(raw_max0 - raw_min0)),
                    int(color[1]*(res1 - raw_min1)/(raw_max1 - raw_min1)),
                    int(color[2]*(res2 - raw_min2)/(raw_max2 - raw_min2))
                    )
            #color_remap = tuple([int(color[n]*(res0 - raw_min0)/(raw_max0 - raw_min0)) for n in range(len(color))]) #use this instead of above for coloration based on one function
            new_img[i, j] = color_remap
    new.save("new_img.png")
    new.show()
    return 


if __name__=="__main__":
    map_colors()
