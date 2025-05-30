import sys

def cutline(lst,n):
    lst.sort(reverse=True)
    return lst[n-1]

if __name__ == "__main__":
    i,n = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(cutline(lst,n))