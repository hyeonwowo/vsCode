import sys

def wine(lst):
    if n == 1:
        return lst[0]
    elif n == 2:
        return lst[0] + lst[1]

    dp = [0] * n
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[0] + lst[2], lst[1] + lst[2], lst[0] + lst[1])
    
    for i in range(3,n):
        dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-1], dp[i-2] + lst[i])
    return dp[n-1]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    print(wine(lst))