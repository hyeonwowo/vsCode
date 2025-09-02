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
    
    xadj = []
    yadj = []
    zadj = []
    for i in range(V):
        for j in range(i+1, V):
            xadj.append((abs(P[i][0] - P[j][0]), i, j))
            yadj.append((abs(P[i][1] - P[j][1]), i, j))
            zadj.append((abs(P[i][2] - P[j][2]), i, j))
    
    xadj.sort()
    yadj.sort()
    zadj.sort()
    
    adj = [[] for _ in range(V)]
    for i in range(V-1): 
        weight, v, w = xadj[i]
        adj[v].append((w, weight))
        adj[w].append((v, weight))
        
        weight, v, w = yadj[i]
        adj[v].append((w, weight))
        adj[w].append((v, weight))
        
        weight, v, w = zadj[i]
        adj[v].append((w, weight))
        adj[w].append((v, weight))
    
    
    total_weight = prim(V, adj)
    print(total_weight)
    # 1, 모든 간선 구하기
    # 2, V-1 만큼의 간선 추리기 (sort())
    # 3. adj 업데이트
    # 4. 크루스칼 돌리기
    