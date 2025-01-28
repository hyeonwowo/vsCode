class Graph:
    def __init__(self, directed=False):
        """
        그래프 생성자
        :param directed: True면 방향 그래프, False면 무방향 그래프
        """
        self.adjacency_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        """
        그래프에 정점을 추가합니다.
        :param vertex: 정점 이름
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v):
        """
        그래프에 간선을 추가합니다.
        :param u: 시작 정점
        :param v: 끝 정점
        """
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)

        self.adjacency_list[u].append(v)
        if not self.directed:
            self.adjacency_list[v].append(u)

    def remove_edge(self, u, v):
        """
        그래프에서 간선을 제거합니다.
        :param u: 시작 정점
        :param v: 끝 정점
        """
        if u in self.adjacency_list and v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v)
        if not self.directed and v in self.adjacency_list and u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)

    def remove_vertex(self, vertex):
        """
        그래프에서 정점을 제거합니다.
        :param vertex: 제거할 정점
        """
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]

        for v in self.adjacency_list:
            if vertex in self.adjacency_list[v]:
                self.adjacency_list[v].remove(vertex)

    def get_vertices(self):
        """
        그래프의 모든 정점을 반환합니다.
        """
        return list(self.adjacency_list.keys())

    def get_edges(self):
        """
        그래프의 모든 간선을 반환합니다.
        """
        edges = []
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                if self.directed or (v, u) not in edges:
                    edges.append((u, v))
        return edges

    def display(self):
        """
        그래프를 보기 좋게 출력합니다.
        """
        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}")

# 예제 사용법
g = Graph(directed=False)  # 무방향 그래프 생성
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.display()

print("Vertices:", g.get_vertices())
print("Edges:", g.get_edges())
