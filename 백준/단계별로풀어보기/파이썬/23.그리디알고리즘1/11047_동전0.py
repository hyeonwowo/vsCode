import sys # 시간초과 발생

def coins(coinlst, k):
    currentcoin = k
    count = 0
    while currentcoin != 0:
        maxcoin = max([coin for coin in coinlst if coin <= currentcoin])
        currentcoin -= maxcoin
        count += 1
    return count

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    coinlst = [int(sys.stdin.readline()) for _ in range(n)]
    print(coins(coinlst,k))