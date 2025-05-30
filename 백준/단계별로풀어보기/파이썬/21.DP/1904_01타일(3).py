import sys

def tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
        
    return dp[n]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(tile(n))