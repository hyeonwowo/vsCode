import sys

def inputnumbercard(n):
    return list(map(int, sys.stdin.readline().split()))

def outputnumbercard(m,lst):
    input = set(lst)
    output = set(list(map(int, sys.stdin.readline().split())))

if __name__ == "__main__":
    lst = inputnumbercard(int(input()))
    outputnumbercard(int(input()),lst)