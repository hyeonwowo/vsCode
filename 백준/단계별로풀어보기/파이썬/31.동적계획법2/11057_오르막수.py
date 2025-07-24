import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    MOD = 10007

    dp = [[0] * 10 for _ in range(n)]

    # 1자리 오르막 수: 0~9 각 1개씩
    for j in range(10):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD # 지금까지 구한거 + 끝자리에 붙여서 새로 만든는거 (점화식 유도는 연습장 7page참고)

    print(sum(dp[n-1]) % MOD)

