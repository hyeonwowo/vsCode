class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        
    def put(self, V, W):
        self.adj[V].append(W)
        self.adj[W].append(V)
        self.E += 1
        
    def DFS(self, v):
        visited = []
        def recur(node):
            if node not in visited:
                visited.append(node)
                for neighbor in self.adj[node]:
                    recur(neighbor)
                    
        recur(v)
        return visited
    
if __name__ == "__main__":
    # 그래프 생성
    g = Graph(6)
    g.put(0, 1)
    g.put(1, 2)
    g.put(1, 3)
    g.put(1, 5)
    g.put(2, 4)
    g.put(4, 5)
    
    print(g.DFS(0))  # DFS 실행