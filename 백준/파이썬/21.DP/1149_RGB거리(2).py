import sys

def RGB_dp(cost):
    dp = [[0]*3 for _ in range(n)]
    dp[0][0] = cost[0][0]  
    dp[0][1] = cost[0][1]  
    dp[0][2] = cost[0][2]  

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    return min(dp[n-1])

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(RGB_dp(cost))
