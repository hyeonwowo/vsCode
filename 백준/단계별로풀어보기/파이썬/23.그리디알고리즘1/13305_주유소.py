import sys

def gasStation(n): # dp문제
    dp = [0] * n
    dp[1] = cost[0] * length[0]
    for i in range(2, n):
        dp[i] = min(dp[i-1] + (cost[i-1] * length[i-1]),
                    dp[i-2] + cost[i-2] * (length[i-2] + length[i-1]))
    return max(dp)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    length = list(map(int, sys.stdin.readline().split()))
    cost = list(map(int, sys.stdin.readline().split()))
    print(gasStation(n))