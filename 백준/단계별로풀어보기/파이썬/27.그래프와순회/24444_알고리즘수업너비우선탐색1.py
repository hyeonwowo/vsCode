import sys
from collections import deque

class Graph:
    def __init__(self, V, E):
        self.v = V
        self.E = E
        self.adj = [[] for _ in range(V+1)]
        self.visited = [0 for _ in range(V+1)]
        self.count = 1
        
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        
    def BFS(self, S):
        queue = deque([S])
        self.visited[S] = self.count
        self.count += 1
        
        while queue:
            node = queue.popleft()
            for neighbor in sorted(self.adj[node]):
                if self.visited[neighbor] == 0:
                    self.visited[neighbor] = self.count
                    self.count += 1 # depth를 찾는게 아닌, 방분순서를 찾음 -> count += 1을 사용 !
                    queue.append(neighbor)

if __name__ == "__main__":
    V, E, S = map(int, sys.stdin.readline().split())
    
    g = Graph(V,E)
    for _ in range(E):
        v, w = map(int, sys.stdin.readline().split())
        g.addEdge(v,w)
        
    g.BFS(S)
    
    for i in range(1,V+1):
        print(g.visited[i])