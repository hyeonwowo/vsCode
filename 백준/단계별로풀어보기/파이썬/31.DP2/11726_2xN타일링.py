import sys

if __name__ == "__main__":
    dp = [0] * 1001
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    
    for i in range(4, 1001):
        dp[i] = dp[i-1] + dp[i-2]
        
    n = int(sys.stdin.readline())
    print(dp[n]%10007)