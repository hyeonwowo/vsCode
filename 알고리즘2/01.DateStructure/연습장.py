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

    