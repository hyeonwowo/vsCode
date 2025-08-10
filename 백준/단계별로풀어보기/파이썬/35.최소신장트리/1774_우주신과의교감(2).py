import sys # prim 728ms
import math
import heapq

def prim_eager(V, adj):
    mst = []
    total_weight = 0.0

    dist = [float('inf')] * V     
    parent = [-1] * V             
    visited = [False] * V

    dist[0] = 0.0
    heap = [(0.0, 0)]             

    while heap:
        key, v = heapq.heappop(heap) 
        if visited[v]:
            continue
        visited[v] = True

        total_weight += key
        if parent[v] != -1:          
            mst.append((parent[v], v, key))

        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                parent[w] = v
                heapq.heappush(heap, (weight, w))

    return total_weight, mst

def distance(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    points = [tuple(map(float, input().split())) for _ in range(n)]

    adj = [[] for _ in range(n)]

    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            w = distance(xi, yi, xj, yj)
            adj[i].append((j, w))
            adj[j].append((i, w))

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((b, 0.0))
        adj[b].append((a, 0.0))

    total_weight, mst = prim_eager(n, adj)

    print(f"{total_weight:.2f}")
