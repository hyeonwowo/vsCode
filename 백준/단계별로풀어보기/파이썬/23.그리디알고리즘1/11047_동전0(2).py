import sys

def coins(k, money):
    money = sorted(money, reverse=True)
    count = 0
    for coin in money:
        if coin <= k:
            count +=  k // coin
            k = k % coin
    return count

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    money = [int(sys.stdin.readline()) for _ in range(n)]
    print(coins(k, money))
