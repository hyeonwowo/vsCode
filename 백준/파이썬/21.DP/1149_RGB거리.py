import sys

def RGB(house):
    maxsum = 0
    prehouse = None
    for i in range(n):
        for j in range(3):
            if prehouse == j:
                house[i][j] = float('inf')
        minvalue = min(house[i])
        maxsum += minvalue
        prehouse = house[i].index(minvalue)
    return maxsum
            
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    house = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(RGB(house))