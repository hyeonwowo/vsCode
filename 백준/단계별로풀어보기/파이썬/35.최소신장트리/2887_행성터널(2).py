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
                heapq.heappush(heap, (weight, w))
                
    return total_weight

if __name__ == "__main__":
    V = int(sys.stdin.readline())
    P = []
    
    for _ in range(V):
        x, y, z = map(int, sys.stdin.readline().split())
        P.append((x, y, z))

    adj = [[] for _ in range(V)]

    # x좌표를 인덱스와 함께 저장
    PX = [(P[i][0], i) for i in range(V)]
    PX.sort()
    for i in range(V-1):
        weight = abs(PX[i][0] - PX[i+1][0])
        v, w = PX[i][1], PX[i+1][1]
        adj[v].append((w, weight))
        adj[w].append((v, weight))
    
    # y좌표를 인덱스와 함꼐 저장
    PY = [(P[i][1], i) for i in range(V)]
    PY.sort()
    for i in range(V-1):
        weight = abs(PY[i][0] - PY[i+1][0])
        v, w = PY[i][1], PY[i+1][1]
        adj[v].append((w, weight))
        adj[w].append((v, weight))
        
    # z좌표를 인덱스와 함께 저장
    PZ = [(P[i][2], i) for i in range(V)]
    PZ.sort()
    for i in range(V-1):
        weight = abs(PZ[i][0] - PZ[i+1][0])
        v, w = PZ[i][1], PZ[i+1][1]
        adj[v].append((w, weight))
        adj[w].append((v, weight))
        
    total_weight = prim(V, adj)
    print(total_weight)