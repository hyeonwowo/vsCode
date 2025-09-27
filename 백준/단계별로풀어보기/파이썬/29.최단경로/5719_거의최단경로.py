import sys
import heapq
from collections import deque

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
        
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
    
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))

def dijkstra(start, graph):
    V = graph.V
    distTo = [float('inf')] * V
    prev = [[] for _ in range(V)]   # 여러 부모 저장
    
    pq = []
    distTo[start] = 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        curr_dist, v = heapq.heappop(pq)
        if distTo[v] < curr_dist:
            continue
        for edge in graph.adj[v]:
            w = edge.w
            if distTo[w] > distTo[v] + edge.weight:
                distTo[w] = distTo[v] + edge.weight
                prev[w] = [v]
                heapq.heappush(pq, (distTo[w], w))
            elif distTo[w] == distTo[v] + edge.weight:
                prev[w].append(v)
    return distTo, prev

def remove_shortest_paths(graph, prev, start, end):
    q = deque([end])
    visited = [False] * graph.V
    while q:
        v = q.popleft()
        if v == start: 
            continue
        for u in prev[v]:
            # 간선 u->v 제거
            graph.adj[u] = [edge for edge in graph.adj[u] if edge.w != v]
            if not visited[u]:
                visited[u] = True
                q.append(u)

if __name__ == "__main__":
    input = sys.stdin.readline
    res = []
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        start, end = map(int, input().split())
        g = Graph(n)
        for _ in range(m):
            v, w, weight = map(int, input().split())
            g.addEdge(v, w, weight)
        
        # 1. 최단 거리
        distTo, prev = dijkstra(start, g)
        
        # 2. 최단 경로 간선 제거
        remove_shortest_paths(g, prev, start, end)
        
        # 3. 다시 다익스트라
        distTo2, _ = dijkstra(start, g)
        res.append(-1 if distTo2[end] == float('inf') else distTo2[end])
    
    for ele in res:
        print(ele)
