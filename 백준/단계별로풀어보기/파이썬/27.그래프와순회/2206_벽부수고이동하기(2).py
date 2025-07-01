import sys
from collections import deque

def BFS():
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 0))  # (x, y, 벽 부쉈는지 여부)
    visited[0][0][0] = True
    depth = [[[1] * 2 for _ in range(m)] for _ in range(n)]
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while queue:
        x, y, broken = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return depth[x][y][broken]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고 아직 방문하지 않은 경우
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    depth[nx][ny][broken] = depth[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                # 벽이고 아직 부수지 않은 경우
                elif grid[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    depth[nx][ny][1] = depth[x][y][broken] + 1
                    queue.append((nx, ny, 1))
    
    return -1  # 도달 불가

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())  # n: 행, m: 열
    grid = [list(map(int, input().strip())) for _ in range(n)]
    print(BFS())
