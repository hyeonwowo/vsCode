import sys
from collections import defaultdict, deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)
    
    def addEdge(self, u, v, weight):
        self.adj[u].append((v, weight))

    def topologicalSort(self):
        indegree = [0] * (self.V + 1)
        for u in self.adj:
            for v, _ in self.adj[u]:
                indegree[v] += 1

        queue = deque()
        for i in range(1, self.V + 1):
            if indegree[i] == 0:
                queue.append(i)

        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, _ in self.adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return topo_order

    def shortestPath(self, start):
        dist = [float('inf')] * (self.V + 1)
        dist[start] = 0

        topo_order = self.topologicalSort()
        for u in topo_order:
            if dist[u] != float('inf'):
                for v, weight in self.adj[u]:
                    if dist[v] > dist[u] + weight:
                        dist[v] = dist[u] + weight

        return dist

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(1, 2, 5)
    g.addEdge(1, 3, 3)
    g.addEdge(2, 4, 6)
    g.addEdge(2, 5, 2)
    g.addEdge(3, 5, 4)
    g.addEdge(5, 4, -1)
    g.addEdge(4, 6, 1)
    g.addEdge(5, 6, 2)

    start = 1
    dist = g.shortestPath(start)

    for v in range(1, g.V + 1):
        if dist[v] == float('inf'):
            print(f"{start} -> {v}: 도달 불가")
        else:
            print(f"{start} -> {v}: 최단 거리 = {dist[v]}")
