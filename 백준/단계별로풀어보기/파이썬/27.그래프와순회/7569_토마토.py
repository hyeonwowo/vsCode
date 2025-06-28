import sys
from collections import deque

def BFS(grid):
    pass

if __name__ == "__main__":
    n, m, h = map(int, sys.stdin.readline().split())
    grid = [list(list(map(int, sys.stdin.readline().split())) for _ in range(m)) for _ in range(h)]
    directions = [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)]
    print(grid)