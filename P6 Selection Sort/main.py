# Selection Sort
# Project 6
# CECS 100
# Name: Rodrigo Becerril Ferreyra
# ID: 017584071
def selection(oldlist, start=-1):
    if start == -1:
        start = 0

    if start == len(oldlist) - 1:
        return oldlist
    else:
        swap = oldlist.index(min(oldlist[start:]))
        oldlist[start] = oldlist[start] + oldlist[swap]
        oldlist[swap] = oldlist[start] - oldlist[swap]
        oldlist[start] = oldlist[start] - oldlist[swap]
        return selection(oldlist, start+1)

def main():
    print(selection([15, 10, 13]))

main()
