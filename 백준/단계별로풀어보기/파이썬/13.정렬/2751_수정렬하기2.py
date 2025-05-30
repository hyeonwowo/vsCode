import sys

def printlst(lst):
    lst.sort()
    for element in lst:
        print(element)
        
if __name__ == "__main__":
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    printlst(lst)