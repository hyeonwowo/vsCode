import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    dp1 = [0] * n
    dp2 = [0] * n
    
    dp1[0] = lst[0]
    dp2[0] = lst[0]
    
    maxval = lst[0]
    for i in range(1, n):
        dp1[i] = max(lst[i], dp1[i-1] + lst[i])
        dp2[i] = max(dp1[i-1], dp2[i-1] + lst[i])
        maxval = max(maxval, dp1[i], dp2[i])
    print(maxval)