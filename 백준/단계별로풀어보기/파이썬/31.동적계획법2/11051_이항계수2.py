import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())

    dp = [[1] * (i+1) for i in range(N+1)]

    for i in range(2, N+1):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    print(dp[N][K]%10007)
