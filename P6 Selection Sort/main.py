# Selection Sort
# Project 6
# CECS 100
# Name: Rodrigo Becerril Ferreyra
# ID: 017584071
def selection(oldlist, start=0):

    if (start <= len(oldlist) - 1) or (len(oldlist) == 0):
        return oldlist
    else:
        swap = oldlist.index(min(oldlist[start:]))
        if oldlist[swap] < oldlist[start]:
            oldlist[start] = oldlist[start] + oldlist[swap]
            oldlist[swap] = oldlist[start] - oldlist[swap]
            oldlist[start] = oldlist[start] - oldlist[swap]
        return selection(oldlist, start+1)

def main():
    print(selection([10, 9, 8, 7, 0, 5, 4, 3, 2, 1]))

main()
