import sys

def sortpoint(n):
    lst = []
    for _ in range(n):
        x,y = map(int,sys.stdin.readline().split())
        lst.append((x,y))
    sort_point = sorted(lst, key=lambda x:(x[0],x[1]))
    return sort_point

def printpoint(lst):
    for element in lst:
        print(*element)
    
if __name__ == "__main__":
    printpoint(sortpoint(int(input())))