import sys

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
        
class Graph:
    def __init__(self, V):
        self.v = V
        self.edges = [] # 간선중심이라 edges 자료구조 사용
        
    def addEdge(self, v, w, weight):
        self.edges.append(Edge(v, w, weight))
        
def bellman_ford(graph, start):
    V = graph.v
    distTo = [float('inf')] * (V+1)
    edgeTo = [None] * (V+1)
    distTo[start] = 0
    
    for _ in range(V-1):
        for edge in graph.edges:
            relax(edge.v, edge.w, edge.weight, distTo, edgeTo)
            
    for edge in graph.edges:
        if relax(edge.u, edge.v, edge.weight, distTo, edgeTo):
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
    g = Graph(5)
    g.add_edge(1, 2, 6)
    g.add_edge(1, 3, 7)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 4, 5)
    g.add_edge(2, 5, -4)
    g.add_edge(3, 4, -3)
    g.add_edge(3, 5, 9)
    g.add_edge(4, 2, -2)
    g.add_edge(5, 4, 7)

    start = 1
    distTo, edgeTo = bellman_ford(g, start)

    if distTo is not None:
        for v in range(1, g.V + 1):
            path = pathTo(edgeTo, v)
            if distTo[v] == float('inf'):
                print(f"{start} -> {v}: 도달 불가")
            else:
                print(f"{start} -> {v}: 거리={distTo[v]}, 경로={path}")
