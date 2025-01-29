class Graph:
    def __init__(self, directed=False):
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