import sys

def mybag(weightvalue):
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        weight, value = weightvalue[i-1]
        for j in range(1, M+1):
            if j >= weight:
                dp[i][j] = max(value + dp[i-1][j - weight], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][M]
    
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    weightvalue = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(mybag(weightvalue)) 
