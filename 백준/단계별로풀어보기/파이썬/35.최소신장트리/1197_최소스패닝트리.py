import sys
import heapq

def prim_eager(V, adj):
    mst = []
    total_weight = 0
    
    dist = [float('inf')] * (V+1)
    #parent = [-1] * (V+1)
    visited = [False] * (V+1)
    
    dist[1] = 0
    heap = [(0,1)]
    
    while heap:
        key, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        
        total_weight += key
        #if parent[-1] != -1:
        #    mst.append((parent[v], v, key))
            
        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                #parent[w] = V
                heapq.heappush(heap, (weight, w))

    return total_weight, mst
    
if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        adj[v].append((w, weight))
        adj[w].append((v, weight))

    total_weight, mst = prim_eager(V, adj)
    print(total_weight)