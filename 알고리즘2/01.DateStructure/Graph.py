class Graph:
    def __init__(self, directed=False): # True면 방향 그래프, False면 무방향 그래프
        self.adjacency_list = {} # 딕셔너리 - {'A': ['B'], 'B': ['A']} 이런식으로 저쟝
        self.directed = directed

    def add_vertex(self, vertex): # vertex 추가
        if vertex not in self.adjacency_list: # vertex는 key 값으로 들어감
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v): # edge 추가 (u - 시작, v - 끝)
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)

        # 방향그래프
        self.adjacency_list[u].append(v) # 방향그래프이면 여기서 끝.

        # 무방향그래프
        if not self.directed: # 방향그래프가 아닐 때. 2-3, 3-2 동일 edge를 두번 저장.
            self.adjacency_list[v].append(u)
            
    def remove_vertex(self, vertex): # vertex 제거
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex] # 큰 줄기 속 해당하는 vertex 삭제

        for v in self.adjacency_list:
            if vertex in self.adjacency_list[v]: # 큰 줄기에 딸려있는 잎들에 있는 해당하는 vertex 삭제
                self.adjacency_list[v].remove(vertex)

    def remove_edge(self, u, v): # edge 제거 (u - 시작, v - 끝)
        if u in self.adjacency_list and v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v) # remove() 함수는 값으로 제거 가능
        if not self.directed and v in self.adjacency_list and u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)

    def get_vertices(self): # Graph 모든 vertex 반환
        return list(self.adjacency_list.keys()) # 배웠던 .keys() 사용

    def get_edges(self): # Graph 모든 edge 반환
        edges = [] 
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                if self.directed or (v, u) not in edges:
                    edges.append((u, v))
        return edges

    def display(self): # 그래프 출력
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
