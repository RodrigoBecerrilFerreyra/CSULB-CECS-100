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
	newlist = oldlist
	if end==-1:
		end = len(newlist)
	
	if end <= 1:
		return newlist
	else:
		for i in range(end-1):
			if newlist[i] > newlist[i+1]:
				newlist[i] = newlist[i] + newlist[i+1]
				newlist[i+1] = newlist[i] - newlist[i+1]
				newlist[i] = newlist[i] - newlist[i+1]

		return bubble(newlist, end-1)

def main():
	list1 = [5, 2, 1, -6, 54, 4, 1, 1]
	print(bubble(list1))
	
main()
