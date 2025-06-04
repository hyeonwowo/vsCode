import sys

# 규칙 ! (점화식)
# n : 자릿수
# 1 2 3 4 5 6 7 8 9 | 끝자리수
# -----------------
# 0 1 1 1 1 1 1 1 1 | 한자리수일 때, 끝자리가 j인 수의 갯수
# 1 1 2 2 2 2 2 2 1 | 두자리수일 때, 끝자리가 j인 수의 갯수
# 1 3 3 4 4 4 4 3 2 | 세자리수일 때, 끝자리가 j인 수의 갯수

# n = 3 일 때, 구하는 방법
# j가 1이면, 두자리수를 가지고 끝자리가 0 혹은 2 일때 끝자리가 1인 세자리수를 만들 수 있음
# 따라서 dp[3][1] = dp[2][0] + dp[2][2]

def easystair(n):
    dp = [[0] * 10 for _ in range(n+1)]
    for i in range(1,10):
        dp[0][i] = 1
    for i in range(1,n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif 1 <= j <= 8:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
    return sum(dp[n-1]) % 1000000000

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(easystair(n))