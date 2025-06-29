import sys # 시간초과 발생
from collections import deque

def BFS(grid):
    queue = deque([(0, 0)])
    visited = [[False] * n for _ in range(m)]  # m행, n열
    depth = [[0] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited[0][0] = True
    depth[0][0] = 0
    
    while queue:
        nodex, nodey = queue.popleft()
        if nodex == m - 1 and nodey == n - 1:
            return depth[nodex][nodey]
        
        for dx, dy in directions:
            mx, my = nodex + dx, nodey + dy
            if 0 <= mx < m and 0 <= my < n:
                if not visited[mx][my] and grid[mx][my] == 0:
                    queue.append((mx, my))
                    visited[mx][my] = True
                    depth[mx][my] = depth[nodex][nodey] + 1
                    
    return float('inf')

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(m)]
    
    minval = float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                res = BFS(grid)
                grid[i][j] = 1
            elif grid[i][j] == 0:
                res = BFS(grid)
        
            if res < minval:
                minval = res
                
    if minval == float('inf'):
        print(-1)
    else:
        print(minval)
