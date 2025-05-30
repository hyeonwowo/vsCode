import sys

def downsort(n):
    lst = list(str(n))
    lst.sort(reverse=True)
    return lst

def printlst(lst):
    for element in lst:
        print(element,end='')

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    printlst(downsort(n))