class Graph:
    def __init__(self, directed=False): # True면 방향 그래프, False면 무방향 그래프
        self.adjacency_list = {} # 딕셔너리 - {'A': ['B'], 'B': ['A']} 이런식으로 저쟝
        self.directed = directed # 방향, 비방향 그래프 설정

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

                # 방향그래프 -> 걸리는 족족 추가, 무방향그래프 -> 중복검사 후 추가
                if self.directed or (v, u) not in edges: # 방향 그래프라면 (u,v)를 그냥 추가. 무방향 그래프라면 (v,u)가 있는지 확인 후 없으면 (u,v)추가
                    edges.append((u, v))
                    # self.directed : 
                    # 방향그래프 일 때, self.directed가 True라면 (u,v)를 바로 추가.
                    # 방향그래프 일 때, (u,v)와 (v,u)가 서로 다른 간선이므로, 중복 검사를 할 필요 없이 추가.

                    # (v,u) not in edges:
                    # 무방향그래프 일 때, (v,u)가 이미 존재하는지 확인 (u,v)와 같은 간선이므로 중복 방지
                    # 무방향그래프 일 때, (v,u)가 존재하지 않는다면, (u,v)를 추가
        return edges

    def display(self): # 그래프 출력
        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}") # {vertex} -> {adjlist[vertex] : 해당하는 key(vertex)의 모든 value 값 [] 형태로 출력}

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
