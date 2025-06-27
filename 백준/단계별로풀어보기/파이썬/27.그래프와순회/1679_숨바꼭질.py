import sys
from collections import deque

class Graph:
    def __init__(self, V):
        self.v = V
        self.adj = [[] for _ in range(k*2)]
        self.visited = [False for _ in range(k*2)]
        self.depth = [0 for _ in range(k*2)]
        
    def addEdge(self,v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        
    def BFS(self, S):
        queue = deque([S])
        
        while queue:
            if self.depth[k] != 0:
                return self.depth[k]
            node = queue.popleft()
            for w in self.adj[node]:
                if not self.visited[w]:
                    queue.append(w)
                    self.visited[w] = True
                    self.depth[w] = self.depth[node] + 1
        
if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    g = Graph(k)
    g.visited[n] = True
    g.depth[n] = 1
    
    for i in range(k):
        g.addEdge(i,i-1)
        g.addEdge(i,i+1)
        g.addEdge(i,2*i)
        
    print(g.BFS(n))
    print(g.visited)