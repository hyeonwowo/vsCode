import sys # Prim
import heapq
import math

def prim_eager(V, adj):
    dist = [float('inf')] * V
    visited = [False] * V
    total_weight = 0
    
    dist[0] = 0
    heap = [(0,0)]
    
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

def distance(x1, y1, x2, y2):
    dx, dy = (x1-x2), (y1-y2)
    return math.sqrt(dx*dx + dy*dy)

if __name__ == "__main__":
    V = int(sys.stdin.readline())
    adj = [[] for _ in range(V)]
    
    vertexPoint = []
    for _ in range(V):
        x, y = map(float, sys.stdin.readline().split())
        vertexPoint.append((x, y))
        
    for i in range(V):
        for j in range(i, V):
            weight = distance(vertexPoint[i][0], vertexPoint[i][1], vertexPoint[j][0], vertexPoint[j][1])
            adj[i].append((j, weight))
            adj[j].append((i, weight))
            
    total_weight = prim_eager(V, adj)
    print(f"{total_weight:.2f}")