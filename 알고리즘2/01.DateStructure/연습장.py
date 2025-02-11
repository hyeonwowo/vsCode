class Graph:
    def __init__(self, directed = False):
        self.adjlist = {}
        self.directed = directed
    def add_vertex(self, element):
        if element not in self.adjlist:
            self.adjlist[element] = []
    def add_edge(self, v, w):
        if v not in self.adjlist:
            self.add_vertex(v)
        if w not in self.adjlist:
            self.add_vertex(w)

        # directed Graph
        self.adjlist[v].append(w)

        # undirected Graph
        if not self.directed:
            self.adjlist[w].append(v)

    def remove_vertex(self, element):
        if element in self.adjlist:
            del self.adjlist[element]

        for v in self.adjlist:
            if element in self.adjlist[v]:
                self.adjlist[v].remove(element)
    
    def remove_edge(self,v,u):
        if v in self.adjlist and u in self.adjlist[v]:
            self.adjlist[v].remove(u)
        if not self.directed and u in self.adjlist and v in self.adjlist[u]:
            self.adjlist[u].remove(v)

    def get_vertices(self):
        return list(self.adjlist.keys())
    
    def get_edges(self):
        edges = set()
        for v in self.adjlist:
            for u in self.adjlist[v]:
                if self.directed:
                    edges.add((v, u))  # 유향 그래프에서는 방향 유지
                else:
                    edges.add(tuple(sorted((v, u))))  # 무향 그래프에서는 정렬하여 추가
        return list(edges)

    
    def display(self):
        for vertex in self.adjlist:
            print(f"{vertex} -> {self.adjlist[vertex]}")

g = Graph(directed=False)
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.display()

print("Vertices:", g.get_vertices())
print("Edges:", g.get_edges())