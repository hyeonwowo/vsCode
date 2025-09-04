import sys
from collections import deque
input = sys.stdin.readline

# BFS: 빙산 덩어리 탐색
def BFS(x, y, visited, grid):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 빙산 녹이기
def meltice(grid):
    melt = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                cnt = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == 0:
                            cnt += 1
                melt[i][j] = cnt

    # 동시에 녹이기
    for i in range(n):
        for j in range(m):
            grid[i][j] = max(0, grid[i][j] - melt[i][j]) # 음수방지를 위한 max

def count_components(grid):
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                BFS(i, j, visited, grid)
                cnt += 1
    return cnt

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    year = 0
    while True:
        comp = count_components(grid)
        if comp == 0:   # 다 녹을 때까지 분리 안 됨
            print(0)
            break
        if comp >= 2:   # 분리된 순간
            print(year)
            break
        meltice(grid)
        year += 1
