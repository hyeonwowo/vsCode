import sys
from collections import deque
sys.setrecursionlimit(10**6)

def BFS(sx, sy, length):
    visited = [[0] * length for _ in range(length)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    queue = []
    queue.append((sx, sy))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            tx, ty = x+dx, y+dy
            if sx <= tx < length and sy <= ty < length:
                if not visited[tx][ty]:
                    visited[tx][ty] = 1
                    queue.append((tx, ty))
                            
def backtracking():
    pass

if __name__ == "__main__":
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
    