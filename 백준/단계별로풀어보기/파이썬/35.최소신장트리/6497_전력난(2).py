import sys # prim 1572ms
import heapq

def primEager(V, adj):
    total_weight = 0
    visited = [False] * V
    dist = [float('inf')] * V
    heap = []

    for s in range(V):                
        if visited[s]:
            continue
        dist[s] = 0
        heapq.heappush(heap, (0, s))
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
    while True:
        line = sys.stdin.readline().split()
        if not line:
            break
        V, E = map(int, line)
        if V == 0 and E == 0:
            break

        adj = [[] for _ in range(V)]
        sum_weight = 0
        for _ in range(E):
            v, w, weight = map(int, sys.stdin.readline().split())
            adj[v].append((w, weight))
            adj[w].append((v, weight))
            sum_weight += weight

        res = primEager(V, adj)       
        print(sum_weight - res)      
