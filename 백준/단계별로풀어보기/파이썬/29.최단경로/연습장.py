import sys
import heapq

class Edge:
    def __init__(self, v, w, weight):
        self.v = v  # from
        self.w = w  # to
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.v = V  # 정점 개수
        self.adj = [[] for _ in range(V + 1)]  # 인접 리스트 사용 (1-indexed)

    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))  # 방향 그래프

def relax(v, w, weight, distTo, edgeTo, pq):
    if distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        heapq.heappush(pq, (distTo[w], w))

def dijkstra(graph, start):
    V = graph.v
    distTo = [float('inf')] * (V + 1)
    edgeTo = [None] * (V + 1)
    distTo[start] = 0

    pq = []
    heapq.heappush(pq, (distTo[start], start))  # (거리, 정점)

    while pq:
        curr_dist, v = heapq.heappop(pq)
        if curr_dist > distTo[v]:
            continue  # 더 긴 거리라면 무시

        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, distTo, edgeTo, pq)

    return distTo, edgeTo

def pathTo(edgeTo, v):
    path = []
    while v is not None:
        path.append(v)
        v = edgeTo[v]
    path.reverse()
    return path

if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    start = int(input())
    g = Graph(V)

    for _ in range(E):
        v, w, weight = map(int, input().split())
        g.addEdge(v, w, weight)

    distTo, edgeTo = dijkstra(g, start)

    if distTo is not None:
        for v in range(1, g.v + 1):
            if distTo[v] == float('inf'):
                print("INF")
            else:
                print(distTo[v])
