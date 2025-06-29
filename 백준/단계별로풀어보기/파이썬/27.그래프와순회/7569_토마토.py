import sys
from collections import deque

def BFS(grid): # n, m, h 순서
    queue = deque()
    visited = [[[False] * n for _ in range(m)] for _ in range(h)]
    depth = [[[0] * n for _ in range(m)] for _ in range(h)]
    
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if grid[i][j][k] == 1:
                    queue.append((i, j, k))
                    visited[i][j][k] = True
    
    while queue:
        ch, cy, cx = queue.popleft()
        for dh, dy, dx in directions:
            nh, ny, nx = ch + dh, cy + dy, cx + dx
            if 0 <= nh < h and 0 <= ny < m and 0 <= nx < n:
                if not visited[nh][ny][nx] and grid[nh][ny][nx] == 0:
                    visited[nh][ny][nx] = True
                    depth[nh][ny][nx] = depth[ch][cy][cx] + 1
                    queue.append((nh, ny, nx))

    maxval = 0
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if grid[i][j][k] == 0 and not visited[i][j][k]:
                    return -1  # 아직 익지 않은 토마토 있음
                maxval = max(maxval, depth[i][j][k])
    
    return maxval

if __name__ == "__main__":
    n, m, h = map(int, sys.stdin.readline().split())  # n: 열, m: 행, h: 높이
    grid = [[list(map(int, sys.stdin.readline().split())) for _ in range(m)] for _ in range(h)]
    directions = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]
    print(BFS(grid))
