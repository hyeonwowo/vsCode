import sys

def distance(chickenlst):
    total = 0
    for hx, hy in housePoint:
        mincand = float('inf')
        for cx, cy in chickenlst:
            mincand = min(mincand, abs(hx - cx) + abs(hy - cy))
        total += mincand
    return total

def chicken(start):
    global minval
    if len(chickenCnt) == m:
        cand = distance(chickenCnt)
        minval = min(minval, cand)
    else:
        for i in range(start, len(chickenPoint)):
            chickenCnt.append(chickenPoint[i])
            chicken(i + 1)
            chickenCnt.pop()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    housePoint = []     # 집 위치
    chickenPoint = []   # 치킨집 위치

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                housePoint.append((i, j))
            elif grid[i][j] == 2:
                chickenPoint.append((i, j))

    minval = float('inf')
    chickenCnt = []
    chicken(0)
    print(minval)
