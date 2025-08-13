import sys
from collections import deque
import heapq

def prim(V, adj):
    visited = [False] * (V + 1)
    dist = [float('inf')] * (V + 1)
    heap = [(0, 1)]
    dist[1] = 0
    
    total_weight = 0
    visited_count = 0
    
    while heap:
        key, v = heapq.heappop(heap)
        
        if visited[v]:
            continue
        
        visited[v] = True
        total_weight += key
        visited_count += 1
        
        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                heapq.heappush(heap, (weight, w))
    
    if visited_count == V:
        return total_weight
    else:
        return -1

def BFS(island_idx, start_x, start_y, cnt, n, m, grid):
    queue = deque([(start_x, start_y)])
    island_idx[start_x][start_y] = cnt
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and island_idx[nx][ny] == -1:
                island_idx[nx][ny] = cnt
                queue.append((nx, ny))

def find_islands(n, m, grid):
    island_idx = [[-1] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and island_idx[i][j] == -1:
                cnt += 1
                BFS(island_idx, i, j, cnt, n, m, grid)
    return island_idx, cnt

def find_bridges(n, m, grid, island_idx, island_count):
    adj = [[] for _ in range(island_count + 1)] 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(n):
        for c in range(m):
            if island_idx[r][c] != -1:
                for dx, dy in directions:
                    length = 0
                    nr, nc = r + dx, c + dy
                    
                    while 0 <= nr < n and 0 <= nc < m:
                        if island_idx[nr][nc] == -1: 
                            length += 1
                            nr += dx
                            nc += dy
                        elif island_idx[nr][nc] != island_idx[r][c]:
                            if length >= 2:
                                from_island = island_idx[r][c]
                                to_island = island_idx[nr][nc]
                                adj[from_island].append((to_island, length))
                                adj[to_island].append((from_island, length))
                            break
                        else:
                            break
                            
    return adj

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    island_idx, island_count = find_islands(n, m, grid)
    adj = find_bridges(n, m, grid, island_idx, island_count)
    
    result = prim(island_count, adj)
    print(result)