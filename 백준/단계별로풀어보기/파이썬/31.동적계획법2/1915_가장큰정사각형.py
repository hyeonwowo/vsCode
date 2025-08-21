import sys

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, list(input().strip()))) for _ in range(n)]

    dp = [[0] * m for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(ans, dp[i][j])

    print(ans * ans)
