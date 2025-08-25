import sys

def findcoin(coins):
    dp = [0] * (k+1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin,k+1):
            dp[i] += dp[i-coin]
    return dp[-1]

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    coins = []
    
    for _ in range(n):
        coins.append(int(sys.stdin.readline()))
        
    print(findcoin(coins))