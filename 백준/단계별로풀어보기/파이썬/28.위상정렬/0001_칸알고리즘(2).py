import sys
import heapq # 같은 진입차수일 때, 작은 노드부터 선택

def kahn_topo_sort(v, adj):
    indegree = [0] * (V+1) # 각 노드별 진입 차수 저장 리스트
    
    # 진입 차수 계산
    for v in range(1, V+1):
        for w in adj[v]:
            indegree[w] += 1
            
    # 우선순위큐에 진입 차수 0인 정점들 삽입
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
        return [] # 사이클 존재시

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(V+1)]
    
    for _ in range(E):
        v, w = map(int, sys.stdin.readline().split())
        adj[v].append(w)
        
    print(*kahn_topo_sort(V, adj)) # 항상 번호 작은 순: [1, 2, 3, 4]
    # input
    # 4 4
    # 1 2
    # 1 3
    # 3 4
    # 2 4