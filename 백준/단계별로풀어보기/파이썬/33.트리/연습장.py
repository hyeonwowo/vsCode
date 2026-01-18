import sys
sys.setrecursionlimit(10**6)
LENGTH = 21

def dfs(v, depth):
    visited[v] = True
    d[v] = depth
    
    for w in graph[v]:
        if visited[w]:
            continue
        parent[w][0] = v
        dfs(w, depth+1)

def set_parent():
    dfs(1, 0)
    for i in range(1, LENGTH):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a
    
    for i in range(LENGTH-1,-1,-1):
        if d[b] - d[a] >= 2**i:
            b = parent[b][i]    
            
    if a == b:
        return a
    
    for i in range(LENGTH-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

if __name__ == "__main__":
    n = int(input())
    parent = [[0] * LENGTH for _ in range(n+1)]
    visited = [False] * (n+1)
    d = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    set_parent()
    m = int(sys.stdin.readline())
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        print(lca(a, b))