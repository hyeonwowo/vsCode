class Graph:
    def __init__(self, directed = False): # True : 방향그래프, False : 무방향그래프
        self.adjacency_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)

        self.adjacency_list[u].append(v)
        if not self.directed:
            self.adjacency_list[v].append(u)

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]

        for v in self.adjacency_list:
            if vertex in self.adjacency_list[v]:
                self.adjacency_list[v].remove(vertex)

    def remove_edge(self, u,v):
        if u in self.adjacency_list and v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v)
        if not self.directed and v in self.adjacency_list and u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)
        
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    
    def get_deges(self):
        edges = []
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                if self.directed or (v, u) not in edges:
                    edges.append((u,v))
        return edges

    def display(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}")


g = Graph(directed = False)
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","C")
g.display()