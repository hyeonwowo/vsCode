import sys

def distance(chickenlst):
    mincand = float('inf')
    for hx, hy in housePoint:
        for cx, cy in chickenlst:
            mincand = min(mincand, abs(hx-cx) + abs(hy-cy))
    return mincand

def chicken(start):
    if len(chickenCnt) == m:
        cand = distance(chickenCnt)
        minval = min(minval, cand)
    else:
        for i in range(start, n):
            chickenCnt.append(chickenPoint[i])
            chicken(i+1)
            chickenCnt.pop()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split()))]
    
    chickenPoint = []
    housePoint = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                chickenPoint.append((i, j))
            elif grid[i][j] == 2:
                housePoint.append((i, j))
                
    minval = float('inf')
    chickenCnt = []
    start = 0 
    chicken(start)
