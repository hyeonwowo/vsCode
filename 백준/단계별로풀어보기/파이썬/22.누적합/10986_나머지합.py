import sys

def remainsum(lst):    
    count = 0
    for m in range(1,len(lst)+1):
        windowslice = sum(lst[:m])
        if windowslice % k == 0:
            count += 1
        for i in range(1, n-m+1):
            windowslice = windowslice - lst[i-1] + lst[i-1+m]
            if windowslice % k == 0:
                count += 1
    return count

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(remainsum(lst))