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
        self.validateInstance(other)
        return self.capacity < other.capacity
    
    def __gt__(self, other):
        self.validateInstance(other)
        return self.capacity > other.capacity
    
    def __eq__(self, other):
        if other == None: return False
        self.validateInstance(other)
        return self.v == other.v and self.w == other.w and self.weight == other.weight
    
    def __str__(self):
        return f"{self.v}->{self.w} ({self.flow}/{self.capacity})"
    
    def __repr__(self):
        return self.__str__()
    
    def other(self, vertex):
        if vertex == self.v: return self.w
        elif vertex == self.w: return self.v
        else: self.invalidIndex(vertex)
        
    def remainingCapacityTo(self, vertex):
        if vertex == self.v: return self.flow
        elif vertex == self.w: return self.capacity - self.flow
        else: self.invalidIndex(vertex)
        
    def addRemainingFlowTo(self, vertex, delta):
        assert isinstance(delta, int) or isinstance(delta, float), f"Delta {delta} is neither an integer nor a floating-point number"
        assert delta <= self.remainingCapacityTo(vertex), f"Delta {delta} is greater than the remaining capacity {self.remainingCapacity(vertex)}"        
        if vertex == self.v: self.flow -= delta
        elif vertex == self.w: self.flow += delta
        else: self.invalidIndex(vertex)
        
    def invalidIndex(self, i):
        assert False, f"Illegal endpoint {i}, which is neither of the two end points {self.v} and {self.w}"
     
    @staticmethod   
    def validateInstance(e):
        assert isinstance(e, FlowEdge), f"e={e} is not an instance of FlowEdge"


class FlowNetwork:
    def __init__(self, V):
        assert isinstance(V, int) and V >= 0, f"V({V}) is not an integer >= 0"
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        self.edges = []
        
    def addEdge(self, e): # addEdge(FlowEdge(0,1,6)) : (v,w,capacity)
        FlowEdge.validateInstance(e)
        assert 0<=e.v and e.v<self.V and 0<=e.w and e.w<self.V, f"Edge endpoints ({e.v},{e.w}) are out of the range 0 to {self.V-1}"
        self.adj[e.v].append(e)
        self.adj[e.w].append(e)
        self.edges.append(e)
        self.E += 1
        
    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for e in self.adj[v]:
                if e.v == v: rtList.append(f"{e}\n")
        return "".join(rtList)
    
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

def findAugementingPathBFS(g, s):
    FlowNetwork.validateInstance(g)
    edgeTo = [None for _ in range(g.V)]
    visited = [False for _ in range(g.V)]
    
    q = Queue()
    q.put(s)
    visited[s] = True
    while not q.empty():
        v = q.get()
        for e in g.adj[v]:
            w = e.other()
            if e.remainingCapacity(w) > 0 and not visited[w]:
                edgeTo[w] = e
                visited[w] = True
                q.put(w)
    return edgeTo, visited

class FordFulkerson:
    def __init__(self, g, s, t):
        FlowNetwork.validateInstance(g)
        assert s>=0 and s<g.V, f"s({s}) is not within 0 ~ {g.V-1}"
        assert t>=0 and t<g.V, f"t({t}) is not within 0 ~ {g.V-1}"
        assert s != t, f"s({s}) and t({t}) must be different"
        
        self.g = g.copy()
        self.s, self.t = s, t
        
        self.flow = 0.0
        while self.hasAugmentingPath():
            minflow = float('inf')
            v = t
            while v != s:
                minflow = min()