from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        
    def put(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
        
    def BFS(self, V):
        visited = []
        queue = deque([V])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                queue.extend(self.adj[node])
        return visited
    
# 그래프 생성
g = Graph(6)
g.put(0, 1)
g.put(1, 2)
g.put(1, 3)
g.put(1, 5)
g.put(2, 4)
g.put(4, 5)

print(g.BFS(0))  # BFS 실행