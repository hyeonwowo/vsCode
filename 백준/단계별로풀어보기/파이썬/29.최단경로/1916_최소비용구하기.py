import sys # bellmanFord : 시간초과

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = []
        
    def addEdge(self, v, w, weight):
        self.edges.append(Edge(v, w, weight))

def relax(v, w, weight, distTo, edgeTo):
    if distTo[v] != float('inf') and distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v 
        return True
    return False

def bellmanFord(start, graph):
    V = graph.V
    distTo = [float('inf')] * (V+1)
    edgeTo = [None] * (V+1)
    distTo[start] = 0
    
    for _ in range(V-1):
        for edge in graph.edges:
            relax(edge.v, edge.w, edge.weight, distTo, edgeTo)
    
    for edge in graph.edges:
        if relax(edge.v, edge.w, edge.weight, distTo, edgeTo):
            return None, None
        
    return edgeTo, distTo

if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    
    g = Graph(V)
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        g.addEdge(v, w, weight)
        
    start, end = map(int, sys.stdin.readline().split())
    
    edgeTo, distTo = bellmanFord(start, g)
    print(distTo[end])