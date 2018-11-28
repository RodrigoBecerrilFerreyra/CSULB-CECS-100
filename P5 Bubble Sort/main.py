# CECS 100 Fall 2018
# Project 5
# "Bubble Sort"
# Start date: 2018-11-27
# End date: 
# Name: Rodrigo Becerril Ferreyra
# ID Number: 017584071
# Description:
# 	Manual bubble sort algorithm

def bubble(oldlist, end=-1):
	"""Usage: newlist = bubble(oldlist)

	Returns a list sorted from least to greatest.
	"""

	# Make end equal to the length of the list if function is called outside of function
	if end==-1:
		end = len(oldlist)
	
	# Base case: the function is finished, and shuld be returned
	if end <= 1:
		return oldlist
	# Recursive case: calculate list and try again	
	else:
		for i in range(end-1):
			if oldlist[i] > oldlist[i+1]:
				# swap oldlist[i] with oldlist[i+1]
				oldlist[i] = oldlist[i] + oldlist[i+1]
				oldlist[i+1] = oldlist[i] - oldlist[i+1]
				oldlist[i] = oldlist[i] - oldlist[i+1]

		return bubble(oldlist, end-1) #recursive (calls itself)

def main():
	print(bubble([5, 2, 6, 1]))
	
main()
