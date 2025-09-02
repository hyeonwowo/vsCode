import sys
import heapq

def prim(V, adj):
    dist = [float('inf')] * V
    visited = [False] * V
    
    dist[0] = 0
    heap = [(0,0)]
    
    total_weight = 0
    while heap:
        key, v = heapq.heappop(heap)
        
        if visited[v]:
            continue
        visited[v] = True
        
        total_weight += key
        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                heapq.heappush(heap, (w, weight))
    
    return total_weight
        
if __name__ == "__main__":
    V = int(sys.stdin.readline())
    
    P = [[] for _ in range(V)]
    for _ in range(V):
        x, y, z = map(int, sys.stdin.readline().split())
        P.append((x, y, z))
        
    