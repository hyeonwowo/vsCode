import sys
import heapq

def prim(V, adj):
    total_weight = 0
    
    dist = [float('inf')] * (V+1) # 거리저장 초기값 : float('inf')
    visited = [False] * (V+1) # 방문여부

    dist[1] = 0
    heap = [(0,1)] # 거리, 시작노드 (heap은 첫번재 인덱스를 기준으로 저장하니 '거리' 먼저 삽입)
    
    while heap:
        key, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True # 꺼낸노드처리
        total_weight += key # 꺼낸노드처리
        
        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight
                heapq.heappush(heap, (weight, w))
    
    return total_weight

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        adj[v].append((w, weight))
        adj[w].append((v, weight))
        
    total_weight = prim(V, adj)
    print(total_weight)