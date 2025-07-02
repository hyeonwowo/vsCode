import sys
import heapq

def kahn(v, adj):
    indegree = [0] * (V+1)
    
    for v in range(1, V+1):
        for w in adj[v]:
            indegree[w] += 1
            
    heap = []
    for i in range(1, V+1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
            
    result = []
    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for w in adj[node]:
            indegree[w] -= 1
            if indegree[w] == 0:
                heapq.heappush(heap, w)
                
    if len(result) == V:
        return result
    else:
        return []

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(V+1)]
    
    for _ in range(E):
        v, w = map(int, sys.stdin.readline().split())
        adj[v].append(w)
        
    print(*kahn(V, adj)) # 항상 번호 작은 순: [1, 2, 3, 4]
    # input
    # 4 4
    # 1 2
    # 1 3
    # 3 4
    # 2 4