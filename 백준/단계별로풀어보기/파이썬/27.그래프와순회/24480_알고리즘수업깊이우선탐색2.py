import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, V, E):
        self.v = V
        self.e = E
        self.adj = [[] for _ in range(V+1)]
        self.visited = [0 for _ in range(V+1)]
        self.order = 1
    
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    def DFS(self, S):
        def recur(v):
            self.visited[v] = self.order
            for w in sorted(self.adj[v], reverse=True):
                if self.visited[w] == 0:
                    self.order += 1
                    recur(w)
        recur(S)

if __name__ == "__main__":
    V, E, S = map(int, sys.stdin.readline().split())
    
    g = Graph(V,E)
    for _ in range(E):
        v, w = map(int, sys.stdin.readline().split())
        g.addEdge(v,w)
        
    g.DFS(S)
    
    for i in range(1, V+1):
        print(g.visited[i])