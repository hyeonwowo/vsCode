import sys # prim 2204ms
import heapq

def prim(V, adj):
    visited = [False] * (V+1)
    dist = [float('inf')] * (V+1)
    heap = [(0,1)]
    
    total_weight = 0
    dist[1] = 0
    cnt = 0
    
    while heap:
        key, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        
        total_weight += key
        cnt += 1
        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                heapq.heappush(heap, (weight, w))
    
    if cnt != V:
        return -1
    else:
        return total_weight

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    weightsum = 0
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        weightsum += weight
        adj[v].append((w, weight))
        adj[w].append((v, weight))
    
    total_weight = prim(V, adj)
    if total_weight == -1:
        print(-1)
    else:
        print(weightsum - total_weight)