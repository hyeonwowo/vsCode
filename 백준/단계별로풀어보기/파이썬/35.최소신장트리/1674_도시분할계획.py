import sys
import heapq

def primEager(V, adj):
    visited = [False] * (V+1)
    dist = [float('inf')] * (V+1)
    heap = [(0,1)]

    dist[1] = 0
    total_weight = 0
    edges = []
    while heap:
        key, v = heapq.heappop(heap)
        
        if visited[v]:
            continue
        visited[v] = True
        
        edges.append(key)
        total_weight += key
        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                heapq.heappush(heap, (weight, w))
        
    return total_weight - max(edges)

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        adj[v].append((w, weight))
        adj[w].append((v, weight))
        
    total_weight = primEager(V, adj)
    print(total_weight) # 현재 mst구성 엣지 weight중 최대값 빼주기
    
    