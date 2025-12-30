# 모든 노드에 대한 깊이를 계산합니다.
# 최소 공통 조상을 찾을 두 노드를 확인합니다.
# 먼저 두 노드의 깊이가 동일하도록 거슬러 올라갑니다.
# 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라갑니다.
# 모든 LCA(a, b) 연산에 대하여 3~4번의 과정을 반복합니다.

import sys
from collections import deque

def LCA(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a
    
def BFS(start):
    queue = deque()
    
    visited[start] = True
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                queue.append(w)
                depth[w] = depth[v] + 1
                parent[w] = v
    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        v, w = map(int, sys.stdin.readline().split())
        adj[v].append(w)
        adj[w].append(v)
        
    visited = [False] * (N+1)
    parent = [1] * (N+1)
    depth = [0] * (N+1)    
    BFS(1) # 깊이 구하기
    
    result = []
    query = int(sys.stdin.readline())
    for _ in range(query):
        a, b = map(int, sys.stdin.readline().split())
        result.append(LCA(a,b))
    
    print(*result, sep='\n')