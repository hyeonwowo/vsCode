import sys
sys.setrecursionlimit(10**6)

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
            for w in self.adj[v]:
                if not self.visited[w]:
                    recur(w)
            self.result.append(v)
        
        for i in range(1, self.v+1):
            if not self.visited[i]:
                recur(i)
                
        return self.result[::-1]
            

if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    
    g = Graph(V, E)
    for _ in range(E):
        v, w = map(int, input().split())
        g.addEdge(v, w)
        
    print(*g.DFS())
