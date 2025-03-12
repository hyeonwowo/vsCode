class Graph:
    def __init__(self,V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        
    def put(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
    
    def DFS(self, v):
        visited = []
        def recur(node):
            if node not in visited:
                visited.append(node)
                for adj in self.adj[node]:
                    recur(adj)
        recur(v)
        return visited
    
g = Graph(6)
g.put(0, 1)
g.put(1, 2)
g.put(1, 3)
g.put(1, 5)
g.put(2, 4)
g.put(4, 5)

print(g.DFS(0))  # DFS 실행