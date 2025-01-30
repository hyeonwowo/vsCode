class Graph:
    def __init__(self, directed=False):
        self.adjlist={}
        self.directed = directed
    def add_vertex(self, vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex] = []
    def add_edge(self,u,v):
        if u not in self.adjlist:
            self.add_vertex(u)
        if v not in self.adjlist:
            self.add_vertex(v)
        
        # Directed Graph
        self.adjlist[u].append(v)

        # Undirected Graph
        if not self.directed:
            self.adjlist[v].append(u)

    def remove_vertex(self, vertex):
        if vertex in self.adjlist:
            del self.adjlist[vertex]
        
        for v in self.adjlist:
            if vertex in self.adjlist[v]:
                self.adjlist[v].remove(vertex)

    def remove_edge(self,u,v):
        if u in self.adjlist and v in self.adjlist[u]:
            self.adjlist[u].remove(v)
        
        if not self.directed and v in self.adjlist and u in self.adjlist[v]:
            self.adjlist[v].remove(u)

    def get_vertices(self):
        return list(self.adjlist.keys())
    
    def get_edges(self):
        edges = []
        for u in self.adjlist:
            for v in self.adjlist[u]:
                if self.directed or (v,u) not in edges:
                    self.edges.append(u,v)

    def display(self):
        for vertex in self.adjlist:
            print(f"{vertex} -> {self.adjlist[vertex]}")

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