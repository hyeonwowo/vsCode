# deque 사용 BFS
from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]

    def put(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def BFS(self, start):
        visited = []  # 방문한 노드를 저장하는 리스트
        queue = deque([start])  # 큐에 시작 노드 추가

        while queue:
            node = queue.popleft()  # 큐에서 노드 꺼내기 : 큐 내부 좌측 element
            if node not in visited:
                visited.append(node)  # 방문 처리
                queue.extend(self.adj[node])  # 인접한 노드들을 큐에 추가

        return visited  # BFS 탐색 순서 반환

# 그래프 생성
g = Graph(6)
g.put(0, 1)
g.put(1, 2)
g.put(1, 3)
g.put(1, 5)
g.put(2, 4)
g.put(4, 5)

print(g.BFS(0))  # BFS 실행
