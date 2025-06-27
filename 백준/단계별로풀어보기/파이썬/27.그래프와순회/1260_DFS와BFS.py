import sys
from collections import deque
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, V, E):
        self.v = V
        self.e = E
        self.adj = [[] for _ in range(V+1)]
        
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)    
    
    def DFS(self, S):
        visited = [0 for _ in range(V+1)]
        res = []
        def recur(v):
            visited[v] = 1
            res.append(v)
            for w in sorted(self.adj[v]):
                if visited[w] == 0:
                    recur(w)
        recur(S)
        return res
    
    def BFS(self, S):
        visited = [0 for _ in range(V+1)]
        res = []
        
        queue = deque([S])
        visited[S] = 1
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for w in sorted(self.adj[node]):
                if visited[w] == 0:
                    queue.append(w)
                    visited[w] = 1
        return res
    
if __name__ == "__main__":
    V, E, S = map(int, sys.stdin.readline().split())
    g = Graph(V, E)
    
    for _ in range(E):
        v, w = map(int, sys.stdin.readline().split())
        g.addEdge(v, w)
        
    dfsRes = g.DFS(S)
    bfsRes = g.BFS(S)
    
    print(*dfsRes)
    print(*bfsRes)