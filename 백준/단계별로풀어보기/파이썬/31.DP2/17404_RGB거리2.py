import sys

def RGB(cost, dp):
    answer = float('inf')
    for start in range(3):
        for i in range(3):
            dp[0][i] = cost[0][i]
        
        for i in range(1, n):
            dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])
            
        for end in range(3):
            if start != end:
                answer = min(answer, dp[n-1][end]) # start인덱스와 다른, 나머지 두개의 인덱스 중 최소값 선택 및 갱신 (1-2, 1-3) (2-1,2-3) (3-1,3-2)
    return answer

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = [[float('inf')] * 3 for _ in range(n)]
    
    print(RGB(cost, dp))