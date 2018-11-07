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
	print("\nEnter the coordinates of your two points as prompted.")
	x1 = float(input("X₁ = "))
	y1 = float(input("Y₁ = "))
	x2 = float(input("X₂ = "))
	y2 = float(input("Y₂ = "))

	m = (y2 - y1)/(x2 - x1)

	# y = m(x - x1) + y1

	x = [-10, 0, 10, x1, x2]
	y = []

	for i in x:
		y.append( (m * (i - x1) ) + y1 )

	plt.plot(x, y, "r")

	if(x1 > 10) or (x2 > 10):
		plt.plot([x[3], x[4]], [y[3], y[4]], "ro")
	else:
		plt.plot([x[0], x[2], x[3], x[4]], [y[0], y[2], y[3], y[4]], "ro")
	plt.show()

def slopeint():
	print("\nEnter the slope and y-intercept of your function as prompted.")
	m = float(input("m = "))
	b = float(input("y = "))

	x = [-10, 0, 10]
	y = [m*x[0]+b, b, m*x[2]+b]
	#for i in x:
	#	y.append(b + (m * i))

	plt.plot(x, y, "ro")
	plt.plot(x, y, "r")
	plt.show()

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
