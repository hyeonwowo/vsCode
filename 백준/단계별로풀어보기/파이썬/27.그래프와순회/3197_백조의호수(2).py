import sys
from collections import deque

def BFS():
    global swanQ, visited
    nextQ = deque()
    while swanQ:
        x, y = swanQ.popleft()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == "X":   
                    nextQ.append((nx, ny))
                else:  
                    swanQ.append((nx, ny))
    swanQ = nextQ
    return False

def melt():
    global waterQ
    for _ in range(len(waterQ)):
        x, y = waterQ.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c:
                if grid[nx][ny] == "X":
                    grid[nx][ny] = "."
                    waterQ.append((nx, ny))

def solve():
    day = 0
    while True:
        if BFS(): 
            return day
        melt() 
        day += 1

if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split())
    grid = [list(input().strip()) for _ in range(r)]
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    swans = []
    waterQ = deque()

    for i in range(r):
        for j in range(c):
            if grid[i][j] != "X":  
                waterQ.append((i, j))
            if grid[i][j] == "L":
                swans.append((i, j))

    start, end = swans
    swanQ = deque([start])
    visited = [[False]*c for _ in range(r)]
    visited[start[0]][start[1]] = True

    print(solve())
