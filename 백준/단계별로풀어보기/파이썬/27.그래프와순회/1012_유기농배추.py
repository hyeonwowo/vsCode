import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                DFS(nx, ny)

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        m, n, k = map(int, sys.stdin.readline().split())  
        grid = [[0] * m for _ in range(n)]               
        visited = [[False] * m for _ in range(n)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        count = 0

        for _ in range(k):
            x, y = map(int, sys.stdin.readline().split()) 
            grid[y][x] = 1 

        for i in range(n):      
            for j in range(m):   
                if grid[i][j] == 1 and not visited[i][j]:
                    DFS(i, j)
                    count += 1
        
        print(count)
