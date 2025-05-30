import sys

def triangle(tri):
    dp = [[0] * (i+1) for i in range(n)]
    dp[0][0] = tri[0][0]
    
    for i in range(1,n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + tri[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + tri[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + tri[i][j]
    return max(dp[n-1])

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(triangle(tri))