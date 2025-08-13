import sys # 856ms
import heapq

def primEager(V, adj):
    total_weight = 0
    visited = [False] * V
    dist = [float('inf')] * V
    dist[0] = 0
    heap = [(0, 0)]

    while heap:
        key, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        total_weight += key

        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                heapq.heappush(heap, (weight, w))

    return total_weight

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    adj = [[] for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            w = grid[i][j]
            adj[i].append((j, w))
            adj[j].append((i, w))
            
    total_weight = primEager(n, adj)
    print(total_weight)
