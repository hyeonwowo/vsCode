import sys
from collections import deque

def BFS():
    visited = [[[False] * 2 for _ in range(n)] for _ in range(m)]
    queue = deque()
    queue.append((0, 0, 0))  # (x, y, 벽 부쉈는지 여부)
    visited[0][0][0] = True
    depth = [[[1] * 2 for _ in range(n)] for _ in range(m)]
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while queue:
        x, y, broken = queue.popleft()
        
        if x == m - 1 and y == n - 1:
            return depth[x][y][broken]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                # 벽이 아니고 방문 안 한 경우
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    depth[nx][ny][broken] = depth[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                # 벽이고 아직 안 부쉈을 경우
                elif grid[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    depth[nx][ny][1] = depth[x][y][broken] + 1
                    queue.append((nx, ny, 1))
    
    return -1  # 도달 불가

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(m)]
    
    print(BFS())
