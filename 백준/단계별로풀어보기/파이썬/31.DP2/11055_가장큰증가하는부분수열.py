import sys

def mostbiglstsum(lst):
    dp = lst[:]
    
    for i in range(1,n):
        for j in range(i):
            if dp[i] > dp[j]:
                dp[i] = max(dp[i], dp[j] + lst[i])
    return max(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    print(mostbiglstsum(lst))