import sys

def inclinestair(stair):
    if n == 1:
        return stair[0]
    if n == 2:
        return stair[0] + stair[1]
    if n == 3:
        return max(stair[0] + stair[2], stair[1] + stair[2])
    
    dp = [0] * n
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i]) # 마지막 계단을 밟는 조건을 여기서 이미 구현했는데 왜 return max(dp)가 안될까 ?
        
    return dp[n-1]

#만약 계단이 4번째까지 있다고 가정했을 때, 3번째 계단까지의 수가 4번째 계단까지의 수보다 더 클 수 있어서 dp[n-1]을 사용
# ex) 1 10 10 1. dp[3] == 20, dp[4] == 12.  원하는 답은 12지만 출력은 20

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    stair = []
    for _ in range(n):
        stair.append(int(sys.stdin.readline()))
    print(inclinestair(stair))