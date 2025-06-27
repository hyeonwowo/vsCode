import sys
from collections import deque

def BFS(x, y):
    visited = [[False] * m for _ in range(n)]
    depth = [[0] * m for _ in range(n)]
    
    queue = deque([(0,0)])
    visited[0][0] = True
    depth[0][0] = 1
    
    while queue:
        nodex, nodey = queue.popleft()
        for direction in directions:
            dx, dy = nodex + direction[0], nodey + direction[1]
            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dx][dy] and grid[dx][dy] == 1: # grid[dx][dy] == 1을 고려해줘야, 갈 수 있는 길만 탐색한다
                    visited[dx][dy] = True
                    depth[dx][dy] = depth[nodex][nodey] + 1
                    queue.append((dx, dy))
    
    if depth[n-1][m-1] != 0:
        return depth[n-1][m-1]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    print(BFS(0,0))
    