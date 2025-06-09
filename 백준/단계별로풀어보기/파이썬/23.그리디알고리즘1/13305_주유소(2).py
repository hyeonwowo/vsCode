import sys

def gasStation(length, cost):
    mincost = cost[0]
    total = mincost * length[0]
    for i in range(1,n-1):
        if cost[i] < mincost:
            mincost = cost[i]
        total += mincost * length[i]
    return total
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    length = list(map(int, sys.stdin.readline().split()))
    cost = list(map(int, sys.stdin.readline().split()))
    print(gasStation(length, cost))