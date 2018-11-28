# CECS 100 Fall 2018
# Project 5
# "Bubble Sort"
# Start date: 2018-11-27
# End date: 
# Name: Rodrigo Becerril Ferreyra
# ID Number: 017584071
# Description:
# 	Manual bubble sort algorithm

def bubble(oldlist, end):
	"""Usage: newlist = bubble(oldlist, len(oldlist))

	Returns a list sorted from least to greatest.
	"""
	if end <= 1:
		return oldlist
	else:
		for i in range(end):
			if oldlist[i] < oldlist[i+1]:
				oldlist[i] = oldlist[i] + oldlist[i+1]
				oldlist[i+1] = oldlist[i] - oldlist[i+1]
				oldlist[i] = oldlist[i] - oldlist[i+1]
		bubble(oldlist, end-1)

def main():
	pass
	
main()
