import sys

def findavg(lst):
    lst.sorted()

if __name__ == "__main__":
    lst = list(map(int, sys.stdin.readline().split()))
    print(findavg(lst))