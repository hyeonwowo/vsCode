import sys # 시간초과
from collections import deque

def melt(grid):
    newgrid = [row[:] for row in grid]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "X":
                for dx, dy in directions:
                    rx, ry = i + dx, j + dy
                    if 0 <= rx < r and 0 <= ry < c:
                        if grid[rx][ry] == "." or grid[rx][ry] == "L":
                            newgrid[i][j] = "."
                            break
    return newgrid

def BFS(grid, start, end):
    queue = deque([start])
    visited = [[False] * c for _ in range(r)]
    visited[start[0]][start[1]] = True
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            rx, ry = x + dx, y + dy
            if 0 <= rx < r and 0 <= ry < c:
                if not visited[rx][ry] and (grid[rx][ry] == "." or grid[rx][ry] == "L"):
                    queue.append((rx, ry))
                    visited[rx][ry] = True
    return visited[end[0]][end[1]]

def solve(grid, start, end):
    cnt = 0
    while True:
        if BFS(grid, start, end):
            return cnt
        grid = melt(grid)
        cnt += 1

if __name__ == "__main__":
    r, c = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(r)]
    
    S_E = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "L":
                S_E.append((i,j))
    
    start, end = S_E
    print(solve(grid, start, end))
