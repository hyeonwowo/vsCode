import sys
import heapq

def prim_eager(V, adj):
    mst = []
    total_weight = 0
    
    parent = [i for i in range(V)]
    dist = [float('inf')] * V
    visited = [False] * V
    
    dist[0] = 0
    heap = [(0,0)] # key, v = mst정줌에서 v까지 갈 수 있는 가장 최소거리, v
    
    while heap:
        key, v = heapq.heappop()
        
        if visited[v]:
            continue
        visited[v] = True
        
        total_weight += key
        if parent[v] != -1:
            mst.append((parent[v], v, weight))
            
        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                parent[w] = V
                heapq.heappush(heap, (weight, w))      
        
    return total_weight, mst      

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(V)]
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        adj[v].append((w, weight))
        adj[w].append((v, weight))

    total_weight, mst = prim_eager(V, adj)

    for v, w, weight in mst:
        print(v, w, weight)
    print(total_weight)
