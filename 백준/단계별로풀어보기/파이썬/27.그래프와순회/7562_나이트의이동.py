import sys
from collections import deque

def BFS(start, end):
    sx, sy = start[0], start[1]
    ex, ey = end[0], end[1]
    
    visited = [[False] * l for _ in range(l)]
    depth = [[0] * l for _ in range(l)]
    
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    depth[sx][sy] = 0
    
    while queue:
        nodex, nodey = queue.popleft()
        if nodex == ex and nodey == ey:
            return depth[nodex][nodey]
        for direction in directions:
            dx, dy = nodex + direction[0], nodey + direction[1]
            if 0 <= dx < l and 0 <= dy < l:
                if visited[dx][dy] == False:
                    visited[dx][dy] = True
                    depth[dx][dy] = depth[nodex][nodey] + 1
                    queue.append((dx, dy))

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    directions = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    result = []
    
    for _ in range(t):
        l = int(sys.stdin.readline())
        start = tuple(map(int, sys.stdin.readline().split()))
        end = tuple(map(int, sys.stdin.readline().split()))
        result.append(BFS(start, end))
        
    for element in result:
        print(element)
        