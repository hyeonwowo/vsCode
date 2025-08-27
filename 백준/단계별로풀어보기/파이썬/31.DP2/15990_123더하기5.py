import sys
MOD = 1000000009

def makenum(k):
    dp = [[0]*4 for _ in range(k+1)]  # dp[i][j]: i를 만들 때 마지막이 j
    if k >= 1:
        dp[1][1] = 1
    if k >= 2:
        dp[2][2] = 1
    if k >= 3:
        dp[3][1] = 1
        dp[3][2] = 1
        dp[3][3] = 1
    
    for i in range(4, k+1):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD
    
    return (dp[k][1] + dp[k][2] + dp[k][3]) % MOD

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        print(makenum(n))
