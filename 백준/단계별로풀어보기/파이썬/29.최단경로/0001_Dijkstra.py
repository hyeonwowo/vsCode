import sys # 0이상의 가중치 모음 - Dijkstra
import heapq

# 1. pq에서 (가장 가까운 정점 v)를 pop, pq는 이미 방문한 visited에서 "갈 수 있는" 정점 후보
# 2. v를 이미 방문했다면 skip
# 3. v와 연결된 간선 (v → w)들에 대해:
#     - distTo[w] > distTo[v] + weight 라면
#         → distTo[w] 갱신
#         → pq에 (distTo[w], w) 삽입
# 4. pq가 빌 때까지 반복

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V + 1)]  # 1-indexed

    def addEdge(self, u, v, weight):
        self.adj[u].append(Edge(u, v, weight))

def relax(u, v, weight, distTo, edgeTo, pq):
    if distTo[u] + weight < distTo[v]:
        distTo[v] = distTo[u] + weight
        edgeTo[v] = u
        heapq.heappush(pq, (distTo[v], v)) # heapq 삽입 발생

def dijkstra(graph, start):
    V = graph.V
    distTo = [float('inf')] * (V + 1)
    edgeTo = [None] * (V + 1)
    distTo[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distTo[u]: # 다익스트라 우선순위큐에는 어떤 정점이 여러번 들어갈 수 있음. 해당 사항 방지
            continue # relax()에서 걸러지기에 없어도 되긴 함. 그러나, 불필요한 연산방지를 위해 해당 코드 작성

        for edge in graph.adj[u]:
            relax(edge.u, edge.v, edge.weight, distTo, edgeTo, pq)

    return distTo, edgeTo

def pathTo(edgeTo, v):
    path = []
    while v is not None:
        path.append(v)
        v = edgeTo[v]
    path.reverse()
    return path

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(1, 2, 2)
    g.addEdge(1, 3, 5)
    g.addEdge(2, 3, 1)
    g.addEdge(2, 4, 2)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 5, 1)
    g.addEdge(4, 6, 4)
    g.addEdge(5, 6, 1)

    start = 1
    distTo, edgeTo = dijkstra(g, start)

    for v in range(1, g.V + 1):
        path = pathTo(edgeTo, v)
        if distTo[v] == float('inf'):
            print(f"{start} -> {v}: 도달 불가")
        else:
            print(f"{start} -> {v}: 거리={distTo[v]}, 경로={path}")
