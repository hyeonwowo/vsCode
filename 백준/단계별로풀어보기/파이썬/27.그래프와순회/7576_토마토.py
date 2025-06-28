import sys
from collections import deque

def BFS(grid):
    queue = deque()
    visited = [[False] * n for _ in range(m)] # n, m
    depth = [[0] * n for _ in range(m)] # n, m
    
    # m, n
    for i in range(m): 
        for j in range(n): 
            if grid[i][j] == 1:
                queue.append((i,j))
                visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny  = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n: # m, n : m-n 순으로 초기화된 visited, grid 배열을 다루니 m n 순으로
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    depth[nx][ny] = depth[x][y] + 1
                    queue.append((nx, ny))
    
    maxval = 0
    # m, n
    for i in range(m): # m : 줄먼저 처리
        for j in range(n): # n : 줄에 있는 요소 처리
            if grid[i][j] == 0 and not visited[i][j]:
                return -1
            maxval = max(maxval, depth[i][j])
    
    return maxval
    
if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split()) # n 은 한줄에 몇개, m은 몇줄
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    print(BFS(grid))
