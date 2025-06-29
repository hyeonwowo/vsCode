import sys
from collections import deque

class Graph:
    def __init__(self, V):
        self.v = V
        self.adj = [[] for _ in range(V + 1)]
        self.color = [0] * (V + 1)
        self.visited = [False] * (V + 1)

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def BFS(self, S):
        queue = deque([S])
        self.color[S] = 1
        self.visited[S] = True

        while queue:
            node = queue.popleft()
            for neighbor in self.adj[node]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.color[neighbor] = -self.color[node]
                    queue.append(neighbor)
                elif self.color[neighbor] == self.color[node]:
                    return False
        return True

    def isBipartite(self):
        for node in range(1, self.v + 1):
            if not self.visited[node]:
                if not self.BFS(node):
                    return "NO"
        return "YES"

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    result = []
    for _ in range(t):
        v, e = map(int, sys.stdin.readline().split())
        g = Graph(v)
        for _ in range(e):
            a, b = map(int, sys.stdin.readline().split())
            g.addEdge(a, b)
        result.append(g.isBipartite())

    print('\n'.join(result))