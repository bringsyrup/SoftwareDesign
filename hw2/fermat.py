#! /bin/env python


def check_fermat(a, b, c, n):
	fermat = a**n + b**n
	if n > 2 and fermat == c**n:
		print "holy moley somethings blah"
	else:
		print "nope he was totally right"

def inputs():
	a = float(raw_input("input a: "))
	b = float(raw_input("input b: "))
	c = float(raw_input("input c: "))
	n = float(raw_input("input n: "))
	return check_fermat(a, b, c, n)

if __name__=="__main__":

	inputs()
