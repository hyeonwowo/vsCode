import sys

def LCS(str1, str2):
    a = len(str1)
    b = len(str2)
    dp = [[0] * b for _ in range(a)] # a - b 순서면 인덱스 에러 발생.
    for i in range(1,a):
        for j in range(1,b):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[a-1][b-1]

if __name__ == "__main__":
    str1 = ' ' + sys.stdin.readline().rstrip()
    str2 = ' ' + sys.stdin.readline().rstrip()
    print(LCS(str1, str2))