import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    dp = [float('inf')] * (k + 1)
    coin = [int(sys.stdin.readline()) for _ in range(n)]

    dp[0] = 0  # 초기값: 0원을 만드는 데 드는 동전 수는 0

    for i in range(1, k + 1):
        for j in range(n):
            if coin[j] <= i:
                dp[i] = min(dp[i], dp[i-coin[j]]+1)
            
    minval = dp[k]
    if minval == float('inf'):
        print(-1)
    else:
        print(minval)
