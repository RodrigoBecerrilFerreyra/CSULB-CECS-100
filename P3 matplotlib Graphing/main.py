# CECS 100 Project 3
# "Graphing a line using matplotlib and pyplot"
# Start date: 06 November 2018
# End date: 08 November 2018
# Name: Rodrigo Becerril Ferreyra
#ID: 017584071

'''
This program is intended to graph the line defined either by two points
or by a slope and a y-intercept. The required parameters will be inputed by the user.
'''

import matplotlib.pyplot as plt

def twopoints():
	print("\ntwo points")

def slopeint():
	print("\nslopeint")

def main():
	print("Plot a graph using pyplot!")
	print("\nEnter a 1 or a 2\n1: Plot a line using two points\n2: Plot a line using a slope and a y-intercept.")
	
	try:
		ui = int(input("\n"))

		if ui == 1:
			twopoints()
		elif ui == 2:
			slopeint()
		else:
			raise(ValueError)

	except ValueError:
		print("Please enter a 1 or a 2!")

main()	
