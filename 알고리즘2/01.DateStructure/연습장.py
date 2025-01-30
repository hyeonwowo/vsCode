class Graph:
    def __init__(self, directed = False):
        self.adjlist = {}
        self.directed = directed
    def add_vertex(self, vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex] = []
    def add_edge(self,u,v):
        if u not in self.adjlist:
            self.add_vertex(u)
        if v not in self.adjlist:
            self.add_vertex(v)
        self.adjlist[u].append(v)

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
    
    def get_deges(self):
        edges = []
        for u in self.adjlist:
            for v in self.adjlist[u]:
                if self.directed or (v,u) not in edges:
                    edges.append((u,v))
        return edges
    
    def display(self):
        for vertex in self.adjlist:
            print(f"{vertex} -> {self.adjlist[vertex]}")
    

g = Graph(direcged = False)
