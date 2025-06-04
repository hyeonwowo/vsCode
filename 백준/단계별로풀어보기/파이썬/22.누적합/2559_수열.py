import sys

def sliceing(lst):
    windowslice = sum(lst[:m])
    maxval = windowslice
    for i in range(1,n-m+1):
        windowslice = windowslice - lst[i-1] + lst[i-1+m]
        if maxval < windowslice:
            maxval = windowslice
    return maxval

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(sliceing(lst))