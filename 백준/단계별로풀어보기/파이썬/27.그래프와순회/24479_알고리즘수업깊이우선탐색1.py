import sys

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.adj = [[] for _ in range(1,V+1)]
        
    def put(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        
    def DFS(self, node):
        visited = []
        def recur(node):
            if node not in visited:
                visited.append(node)
                for neighbor in self.adj[node]:
                    recur(neighbor)
                    
        recur(node)
        return visited
    
if __name__ == "__main__":
    n, m, r = map(int, sys.stdin.readline().split())
    g = Graph(n,m)
    for _ in range(m):
        v, w = map(int, sys.stdin.readline().split())
        g.put(v,w)
        
    print(g.DFS(1))
    
    