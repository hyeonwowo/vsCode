import sys

# 1. 시작 정점의 거리(distTo[start])를 0으로 초기화, 나머지는 ∞로 초기화
# 2. (V - 1)번 반복:
#     - 모든 간선 (v → w, weight)에 대해:
#         - distTo[w] > distTo[v] + weight 만족 시:
#             → distTo[w] = distTo[v] + weight 로 갱신
# 3. 모든 간선 (v → w, weight)에 대해 한 번 더 검사:
#     - 만약 distTo[w] > distTo[v] + weight 여전히 성립한다면
#         → 음수 사이클 존재 → 실패 처리
# 4. 성공적으로 종료 시, distTo 배열이 최단 거리


class Edge:
    def __init__(self, v, w, weight):
        self.v = v  # from
        self.w = w  # to
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = []

    def addEdge(self, v, w, weight):
        self.edges.append(Edge(v, w, weight))

def relax(v, w, weight, distTo, edgeTo):
    # 목적 : 출발점에서 v까지 도달한 적이 있는 경우에만 w갱신
    if distTo[v] != float('inf') and distTo[v] + weight < distTo[w]: # 순회하는 위치의 노드를 방문한 적이 없다면 (distTo[v] != float('inf')) 스킵
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        return True
    return False

def bellman_ford(graph, start):
    V = graph.V
    edgeTo = [None] * (V + 1)
    distTo = [float('inf')] * (V + 1)
    distTo[start] = 0

    for _ in range(V - 1): # BellmanFord 에선 V - 1번 탐색 : 정점이 V개 있으면, 최단경로에서 지나가는 간선은 최대 V - 1개 -> 따라서 최단 거리 정보는 V-1번의 Relaxaion 수행
        for edge in graph.edges: # 각 횟수마다 모든 간선을 한바퀴 다 돈다. 이걸 V - 1 번 반복
            relax(edge.v, edge.w, edge.weight, distTo, edgeTo)

    for edge in graph.edges: # 다시 한번 더 Relax 하는 이유 : 만약 위의 V - 1번 반복 이후에도 어떤 간선이 더 짧은 거리로 갱신될 수 있다면? -> "음수 사이클 존재"
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
    g = Graph(5)
    g.addEdge(1, 2, 6)
    g.addEdge(1, 3, 7)
    g.addEdge(2, 3, 8)
    g.addEdge(2, 4, 5)
    g.addEdge(2, 5, -4)
    g.addEdge(3, 4, -3)
    g.addEdge(3, 5, 9)
    g.addEdge(4, 2, -2)
    g.addEdge(5, 4, 7)

    start = 1
    distTo, edgeTo = bellman_ford(g, start)

    if distTo is not None:
        for v in range(1, g.V + 1):
            path = pathTo(edgeTo, v)
            if distTo[v] == float('inf'):
                print(f"{start} -> {v}: 도달 불가")
            else:
                print(f"{start} -> {v}: 거리={distTo[v]}, 경로={path}")
