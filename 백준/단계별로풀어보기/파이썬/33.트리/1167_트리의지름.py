import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.v = V
        self.adj = [[] for _ in range(self.v + 1)]

    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))

    def BFS(self, start):
        visited = [False] * (self.v + 1)
        dist = [0] * (self.v + 1)

        queue = deque([start])
        visited[start] = True
        max_node = start

        while queue:
            node = queue.popleft()
            for edge in self.adj[node]:
                if not visited[edge.w]:
                    visited[edge.w] = True
                    dist[edge.w] = dist[node] + edge.weight
                    queue.append(edge.w)
                    if dist[edge.w] > dist[max_node]:
                        max_node = edge.w

        return max_node, dist[max_node]  # 가장 먼 노드, 그 거리

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    graph = Graph(n)

    for _ in range(n):
        query = list(map(int, sys.stdin.readline().split()))
        v = query[0]
        i = 1
        while query[i] != -1:
            w = query[i]
            weight = query[i + 1]
            graph.addEdge(v, w, weight)
            i += 2

    # 아무 노드에서 가장 먼 노드 A를 찾는다
    far_node, _ = graph.BFS(1)

    # A에서 가장 먼 노드까지의 거리 → 트리의 지름
    _, diameter = graph.BFS(far_node)

    print(diameter)
