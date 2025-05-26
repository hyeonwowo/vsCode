import sys

def RGB(cost):
    house = [[0]*3 for _ in range(n)]
    house[0][0], house[0][1], house[0][2] = cost[0][0], cost[0][1], cost[0][2]
    
    for i in range(1,n):
        house[i][0] = min(house[i-1][1],house[i-1][2]) + cost[i][0]
        house[i][1] = min(house[i-1][0],house[i-1][2]) + cost[i][1]
        house[i][2] = min(house[i-1][0],house[i-1][1]) + cost[i][2]
    
    return min(house[n-1])

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(RGB(cost))