import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    MOD = 1000000000

    # dp[k][n] = k개의 정수로 n을 만드는 경우의 수
    dp = [[0] * (N + 1) for _ in range(K + 1)]

    # K=1, N을 만드는 경우의 수는 한 가지 (자기 자신)
    for n in range(N + 1):
        dp[1][n] = 1

    # K=0, N=0을 만드는 경우의 수는 한 가지 (아무것도 더하지 않음)
    for k in range(K + 1):
        dp[k][0] = 1

    # DP 테이블 채우기
    for k in range(2, K + 1):
        for n in range(1, N + 1):
            dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % MOD

    print(dp[K][N])