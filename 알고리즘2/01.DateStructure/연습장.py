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

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]

        for v in self.adjacency_list:
            if vertex in self.adjacency_list[v]:
                self.adjacency_list[v].remove(vertex)
    
    def remove_edge(self,u,v):
        if u in  self.adjacency_list and v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v)
        if not self.directed and v in self.adjacency_list and u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    

