import sys

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
        
def relax(v, w, weight, edgeTo, distTo):
    if distTo[w] > distTo[v] + weight:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        return True
    return False
        
def bellmanFord(graph):
    edgeTo = [None] * (graph.V + 1)
    distTo = [float('inf')] * (graph.V + 1)
    distTo[start] = 0
    
    for _ in range(graph.V-1):
        for edge in graph.edges:
            relax(edge.v, edge.w, edge.weight, edgeTo, distTo)
    
    for edge in graph.edges:
        if relax(edge.v, edge.w, edge.weight, edgeTo, distTo):
            return None, None
    
    return edgeTo, distTo

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    start = 1
    
    graph = Graph(V)
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        graph.addEdge(v, w, weight)
        
    edgeTo, distTo = bellmanFord(graph)
    
    if edgeTo == None:
        print(-1)
    else:
        for i in range(2, V+1):
            if distTo[i] == float('inf'):
                print(-1)
            else:
                print(distTo[i])        