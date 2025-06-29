import sys
from collections import deque

class Graph:
    def __init__(self, V, E):
        self.v = V
        self.e = E
        self.adj = [[] for _ in range(1, V+1)]
        self.color = [[] for _ in range(1, V+1)]
        self.visited = [[False] for _ in range(1, V+1)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        
    def DFS(self, S):
        def recur(v):
            for w in self.adj[v]:
                if not self.visited[w]:
                    self.visited[w] = True
                    self.color[w] = -self.color[v]
                    recur(w)
        self.color[S] = 1
        self.visited[S] = True
        recur(S)
    
    def BFS(self, S):
        queue = deque([S])
        self.visited[S] = True
        self.color[S] = 1
        
        while queue:
            node = queue.popleft()
            for w in self.adj[node]:
                if not self.visited[w]:
                    self.visited[w] = True
                    self.color[w] = -self.color[node]
                    queue.append(w)
    
    def search(self, S):
        queue = deque([S])
        self.visited[S] = True
        
        while queue:
            node = queue.popleft()
            for w in self.adj[node]:
                if not self.visited[w] and self.color[node] != self.color[w]:
                    self.visited[w] = True
                    queue.append(w)
                else:
                    return "NO"
        return "YES"
    
if __name__ == "__main__":
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        v, e = map(int, sys.stdin.readline().split())
        g = Graph(v, e)
        
        for _ in range(e):
            v, w = map(int, sys.stdin.readline().split())
            g.addEdge(v, w)
            
        g.BFS(1)
        print(g.search(1))
        