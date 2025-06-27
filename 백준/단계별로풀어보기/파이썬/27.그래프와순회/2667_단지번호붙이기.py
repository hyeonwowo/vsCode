import sys
sys.setrecursionlimit(10**6)

def DFS(i, j):
    count = 1
    visited[i][j] = True
    
    for dx, dy in directions:
        mx, my = i + dx, j + dy
        if 0 <= mx < n and 0 <= my < n:
            if not visited[mx][my] and grid[mx][my] == 1:
                count += DFS(mx, my)
                
    return count
    

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    
    result = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                result.append(DFS(i, j))
                
    result.sort()
    
    print(len(result))
    for cnt in result:
        print(cnt)