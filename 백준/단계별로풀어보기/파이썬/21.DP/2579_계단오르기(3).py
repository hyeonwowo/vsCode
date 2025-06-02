import sys

def inclinestair(stair):
    dp = [0] * n
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])
    
    return max(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    stair = []
    for _ in range(n):
        stair.append(int(sys.stdin.readline()))
    print(inclinestair(stair))