import sys

class Graph:
    def __init__(self, V, E):
        self.v = V
        self.e = E
        self.adj = [[] for _ in range(V+1)]
        self.visited = [False] * (V+1)
        self.result = []
    
    def addEdge(self, v, w):
        self.adj[v].append(w)
    
    def DFS(self):
        def recur(v):
            self.visited[v] = True
            for w in sorted(self.adj[v]):
                if not self.visited[w]:
                    recur(w)
            self.result.append(v)
        
        for i in range(1, self.v + 1):
            if not self.visited[i]:
                recur(i)
                
        return self.result[::-1]
            
if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    g = Graph(V, E)
    for _ in range(E):
        v, w = map(int, sys.stdin.readline().split())
        g.addEdge(v, w)
        
    print(*g.DFS())