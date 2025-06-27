import sys
from collections import deque

class Graph:
    def __init__(self, V, E):
        self.v = V
        self.e = E
        self.adj = [[] for _ in range(V+1)]
        self.visited = [0 for _ in range(V+1)]
        
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        
    def Virus(self, S):
        queue = deque([S])
        self.visited[S] = 1
        
        while queue:
            node = queue.popleft()
            for w in self.adj[node]:
                if self.visited[w] == 0:
                    self.visited[w] = 1
                    queue.append(w)
        
if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    g = Graph(V,E)
    
    for _ in range(E):
        v, w = map(int, sys.stdin.readline().split())
        g.addEdge(v, w)
        
    g.Virus(1)
    print(sum(g.visited)-1)
    