import sys
import heapq

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
        
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(self.V+1)]
        
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))
        
def dijkstra(graph, start):
    distTo = []
    edgeTo = []
    visited = []    
    pq = []
    
    distTo[start] = 0
    heapq.heappush(pq, ())
    
    while pq:
        dist, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        
        for edge in graph.adj[node]:
            if distTo[edge.w] > distTo[edge.v] + edge.weight:
                distTo[edge.w] = distTo[edge.v] + edge.weight
                edgeTo[edge.w] = edge.v
                heapq.heappush(pq, (distTo[edgeTo.w], edge.w))
    
    return distTo, edgeTo


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        V, E, t = map(int, sys.stdin.readline().split())
        s, g, h = map(int, sys.stdin.readline().split())
        graph = Graph(V)
        
        for _ in range(E):
            v, w, weight = map(int, sys.stdin.readline().split())
            graph.addEdge(v, w, weight)
        
        destnation = []
        for _ in range(t):
            destnation.append(int(sys.stdin.readline()))
            
        res = []
        for i in range(t):
            e = destnation[i]
            s_g = dijkstra(graph, s)
            g_h = dijkstra(graph, g)
            h_e = dijkstra(graph, h)
            
            s_h = dijkstra(graph, s)
            h_g = dijkstra(graph, h)
            g_e = dijkstra(graph, g)
            
            road_gh = s_g[g] + g_h[h] + h_e[e]
            road_hg = s_h[h] + h_g[g] + g_e[e]
            res.append(min(road_gh, road_hg))
            
        print(*sorted(res))