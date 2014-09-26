#! /bin/env python

import argparse as ap

def is_between(x, y, z):
    input_array = [x, y, z]
    for item in input_array:
        if type(item) not in [int, float]:
            print "type error: inputs must be integers or floats"
            return None
    if x < z and y > x:
        return True
    else:
        return "you are an idiot"

if __name__=="__main__":
	parser = ap.ArgumentParser(
			description = "blah"
			)
	parser.add_argument("xyz",
			type = float,
			nargs = "+",
			help = "input x y and z separated by a space"
			)
	args = parser.parse_args()
	print is_between(args.xyz[0], args.xyz[1], args.xyz[2])
