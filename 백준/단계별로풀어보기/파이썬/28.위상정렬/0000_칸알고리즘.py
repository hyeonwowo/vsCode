import sys
from collections import deque # 같은 진입차수일 때, 무작위 선택

def kahn_topo_sort(v, adj):
    indegree = [0] * (V+1) # 각 노드의 진입차수 저장 리스트
    
    # 진입 차수 계산
    for v in range(1, V+1):
        for w in adj[v]:
            indegree[w] += 1
            
    # 진입 차수 0인 노드 큐에 삽입
    queue = deque()
    for i in range(1, V+1):
        if indegree[i] == 0:
            queue.append(i)
            
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for w in adj[node]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
                
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
        
    print(kahn_topo_sort(V, adj)) # 결과: [1, 3, 4, 2] 또는 [1, 2, 3, 4] 등
    # input
    # 4 4
    # 1 2
    # 1 3
    # 3 4
    # 2 4