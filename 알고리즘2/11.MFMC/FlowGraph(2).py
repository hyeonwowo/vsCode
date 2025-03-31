from pathlib import Path
from queue import Queue
import timeit

class FlowEdge:
    def __init__(self, v, w, capacity):
        assert isinstance(v, int) and isinstance(w, int), f"v({v}) and/or w({w}) are not integers"
        assert v>=0 and w>=0, f"Vertices {v} and/or {w} have negative IDs"
        assert isinstance(capacity, int) or isinstance(capacity, float), f"Capacity {capacity} is neither an integer nor a floating-point number"
        assert capacity>=0, f"Edge capacity {capacity} must be >= 0"
        self.v, self.w, self.capacity = v, w, capacity
        self.flow = 0.0
        
    def __lt__(self, other):
        return self.capacity < other.capacity
    
    def __gt__(self, other):
        return self.capacity > other.capacity
    
    def __eq__(self, other):
        if other == None: return False
        return self.v == other.v and self.w == other.w and self.capacity == other.capacity
    
    def __str__(self):
        return f"{self.v} -- {self.flow}/{self.capacity} -- {self.w}"
    
    def __repr__(self):
        return self.__str__()
    
    def other(self, vertex):
        if self.v == vertex: return self.w
        elif self.w == vertex: return self.v
        
    def remainingCapacityTo(self, vertex, delta):
        assert isinstance(delta, int) or isinstance(delta, float), f"Delta {delta} is neither an integer nor a floating-point number"
        assert delta <= self.remainingCapacityTo(vertex), f"Delta {delta} is greater than the remaining capacity {self.remainingCapacity(vertex)}"        
        if vertex == self.v: self.flow -= delta
        elif vertex == self.w: self.flow += delta
        
class FlowNetwork:
    def __init__(self, V):
        assert isinstance(V, int) and V >= 0, f"V({V}) is not an integer >= 0"
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        self.edges = []
        
    def addEdge(self, edge): # addEdge(FlowEdge(0,1,6))
        self.adj[edge.v].append(edge)
        self.adj[edge.w].append(edge)
        self.edges.append(edge)
        self.E += 1
        
    def __str__(self): # 모든 정방향 간선 출력
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                if e.v == v: edges.append(f"{e}\n")
        return "".join(edges)
    
    def copy(self):
        fn = FlowNetwork(self.V)
        for e in self.edges: fn.addEdge(FlowEdge(e.v, e.w, e.capacity))
        return fn
    
    @staticmethod
    def fromFile(fileName):
        filePath = Path(__file__).with_name(fileName)   # Use the location of the current .py file   
        with filePath.open('r') as f:
            phase = 0
            line = f.readline().strip() # Read a line, while removing preceding and trailing whitespaces
            while line:                                
                if len(line) > 0:
                    if phase == 0: # Read V, the number of vertices
                        g = FlowNetwork(int(line))
                        phase = 1
                    elif phase == 1: # Read edges
                        edge = line.split()
                        assert len(edge) == 3, f"Invalid edge format found in {line}"
                        if edge[2] == 'inf': g.addEdge(FlowEdge(int(edge[0]), int(edge[1]), float('inf')))                        
                        else: g.addEdge(FlowEdge(int(edge[0]), int(edge[1]), float(edge[2])))                        
                line = f.readline().strip()
        return g

    @staticmethod
    def validateInstance(g):
        assert isinstance(g, FlowNetwork), f"g={g} is not an instance of FlowNetwork"


def findAugmentingPathBFS(g, s):
    edgeTo = [None for _ in range(g.V)]
    visited = [False for _ in range(g.V)]
    
    queue = Queue()
    queue.put(s)
    visited[s] = True
    
    while not queue.empty():
        v = queue.get()
        for e in g.adj[v]:
            w = e.other(v)
            if not visited[w] and e.remainingCapacityTo(w) > 0:
                queue.put(w)
                visited[w] = True
                edgeTo[w] = e
    return edgeTo, visited

class FordFulkerson:
    def __init__(self, g, s, t):
        assert s>=0 and s<g.V, f"s({s}) is not within 0 ~ {g.V-1}"
        assert t>=0 and t<g.V, f"t({t}) is not within 0 ~ {g.V-1}"
        assert s != t, f"s({s}) and t({t}) must be different"
        
        self.g = g.copy()
        self.s, self.t = s, t
        self.flow = 0.0
        
        while self.hasAugmentingPath():
            pass
        
    def hasAugmentingPath(self):
        edgeTo = [None for _ in range(self.g.V)]
        visited = [False for _ in range(self.g.V)]
        
        queue = Queue()
        queue.put(self.s)
        self.visited[self.s] = True
        while not queue.empty():
            v = queue.get()
            for e in self.g.adj[v]:
                w = e.other(v)
                if not self.visited[w] and e.remainingCapacityTo(w) > 0:
                    queue.put(w)
                    self.edgeTo[w] = e
                    self.visited[w] = True
        return self.visited[self.t]  
         