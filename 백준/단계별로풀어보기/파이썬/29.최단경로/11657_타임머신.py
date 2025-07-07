import sys # 벨만포드

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.v = V
        self.edges = []

    def addEdge(self, v, w, weight):
        self.edges.append(Edge(v, w, weight))

# ✅ bellmanFord 함수 내부에서 직접 relax 조건 처리 (relax 함수 제거됨)  # <-- 수정
def bellmanFord(start, graph):
    V = graph.v
    distTo = [float('inf')] * (V + 1)
    distTo[start] = 0

    # ✅ edgeTo 제거됨: 문제에서 경로 출력 요구 없음  # <-- 수정
    for _ in range(V - 1):
        for edge in graph.edges:
            if distTo[edge.v] != float('inf') and distTo[edge.v] + edge.weight < distTo[edge.w]:  # <-- 수정
                distTo[edge.w] = distTo[edge.v] + edge.weight  # <-- 수정

    # ✅ 음수 사이클 감지: dist[v] + weight < dist[w] 이 여전히 성립하면 사이클 존재  # <-- 수정
    for edge in graph.edges:
        if distTo[edge.v] != float('inf') and distTo[edge.v] + edge.weight < distTo[edge.w]:  # <-- 수정
            return None  # 음수 사이클 존재 → None 반환  # <-- 수정

    return distTo  # edgeTo 제거됨  # <-- 수정

if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    graph = Graph(V)

    for _ in range(E):
        v, w, weight = map(int, input().split())
        graph.addEdge(v, w, weight)

    distTo = bellmanFord(1, graph)  # 시작 노드는 1번 도시로 고정

    if distTo is None:
        print(-1)  # ✅ 음수 사이클 존재 시 -1 출력 후 종료  # <-- 수정
    else:
        for i in range(2, V + 1):  # ✅ 2번 노드부터 V번까지 출력  # <-- 수정
            print(distTo[i] if distTo[i] != float('inf') else -1)  # ✅ 도달 불가 시 -1 출력  # <-- 수정
