#! /bin/env python

'''
create grid using python print statements
'''
def grid(dims, length):
	'''prints a boring grid thing with arbitrary square dimensions'''

	horiz = "+ " + "- "*(length)
	vert = "| " + " "*(length*2)

	for i in range(dims):
		if i == dims-1:
			print horiz*(dims-1) + "+"
		else:
			print horiz*(dims-1) + "+"
			for j in range(length):
				print vert*dims
				if j == dims:
					print "|"

if __name__=="__main__":

	grid(8, 3)
