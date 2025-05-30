import sys

def LCS(str1, str2):
    str1 = ' ' + str1
    str2 = ' ' + str2
    n = len(str1)
    m = len(str2)

    dp = [[0] * m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n - 1][m - 1]

if __name__ == "__main__":
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    print(LCS(str1, str2))
