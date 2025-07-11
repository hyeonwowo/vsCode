import sys # g-h 간선을 포함한 경로가 최단거리라면 정답에 포함
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
        self.adj[w].append(Edge(w, v, weight))  # 양방향 도로

def dijkstra(graph, start):
    distTo = [float('inf')] * (graph.V + 1)
    visited = [False] * (graph.V + 1)
    pq = []
    
    distTo[start] = 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        dist, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        
        for edge in graph.adj[node]:
            if distTo[edge.w] > distTo[edge.v] + edge.weight:
                distTo[edge.w] = distTo[edge.v] + edge.weight
                heapq.heappush(pq, (distTo[edge.w], edge.w))
    
    return distTo

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        V, E, t = map(int, sys.stdin.readline().split())
        s, g, h = map(int, sys.stdin.readline().split())
        graph = Graph(V)

        weight_gh = None  # g-h 간선 weight 저장

        for _ in range(E):
            v, w, weight = map(int, sys.stdin.readline().split())
            graph.addEdge(v, w, weight)
            if (v == g and w == h) or (v == h and w == g):
                weight_gh = weight

        destnation = []
        for _ in range(t):
            destnation.append(int(sys.stdin.readline()))
        
        dist_s = dijkstra(graph, s)
        dist_g = dijkstra(graph, g)
        dist_h = dijkstra(graph, h)

        result = []
        for e in destnation:
            path1 = dist_s[g] + weight_gh + dist_h[e]
            path2 = dist_s[h] + weight_gh + dist_g[e]
            # g-h 간선을 포함한 경로가 실제 최단거리라면 정답
            if dist_s[e] == path1 or dist_s[e] == path2:
                result.append(e)
        
        print(*sorted(result))
