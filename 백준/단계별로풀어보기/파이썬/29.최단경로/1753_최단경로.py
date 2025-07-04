import sys # Bellman-Ford 알고리즘 (시간초과)

class Edge:
    def __init__(self, v, w, weight):
        self.v = v  # from
        self.w = w  # to
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.v = V  # 정점 개수
        self.edges = []

    def addEdge(self, v, w, weight):
        self.edges.append(Edge(v, w, weight))

def relax(v, w, weight, distTo, edgeTo):
    if distTo[v] != float('inf') and distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        return True
    return False

def bellman_ford(graph, start):
    V = graph.v
    edgeTo = [None] * (V + 1)
    distTo = [float('inf')] * (V + 1)
    distTo[start] = 0

    for _ in range(V - 1):  # V - 1번 반복
        for edge in graph.edges:  # 모든 간선에 대해 relax
            relax(edge.v, edge.w, edge.weight, distTo, edgeTo)

    for edge in graph.edges:  # 음수 사이클 확인
        if relax(edge.v, edge.w, edge.weight, distTo, edgeTo):
            print("(-) Cycle")
            return None, None

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

    distTo, edgeTo = bellman_ford(g, start)

    if distTo is not None:
        for v in range(1, g.v + 1):
            if distTo[v] == float('inf'):
                print("INF")
            else:
                print(distTo[v])
