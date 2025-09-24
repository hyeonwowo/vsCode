import sys
from collections import deque

def BFS(i, j, grid, n, m):
    visited = [[False] * m for _ in range(n)]
    distTo = [[0] * m for _ in range(n)]
    queue = deque([(i, j)])

    visited[i][j] = True
    distTo[i][j] = 0

    maxval = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            rx, ry = x+dx, y+dy
            if 0 <= rx < n and 0 <= ry < m:
                if not visited[rx][ry] and grid[rx][ry] == 'L':
                    visited[rx][ry] = True
                    distTo[rx][ry] = distTo[x][y] + 1
                    queue.append((rx, ry))
                    maxval = max(maxval, distTo[rx][ry])
    return maxval    

def solve(grid, n, m):
    maxval = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'L':
                cand = BFS(i, j, grid, n, m)
                maxval = max(maxval, cand)
    return maxval

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
    print(solve(grid, n, m))
