import sys
import heapq

def prim_eager(V, adj):
    mst = []
    total_weight = 0

    dist = [float('inf')] * V        
    parent = [-1] * V         
    visited = [False] * V

    dist[0] = 0
    heap = [(0, 0)]          

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
    

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        v, w, weight = map(int, sys.stdin.readline().split())
        adj[v].append((w, weight))
    
    total_weight, mst = prim_eager(1, adj)