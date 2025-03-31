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
        
    def remainingCapacity(self, vertex):
        if self.v == vertex: return self.flow
        elif self.w == vertex: return self.capacity - self.flow
        
    def addRemainingFlowTo(self, vertex, delta):
        if self.v == vertex: self.flow -= delta
        elif self.w == vertex: self.flow += delta
        
class FlowNetwork:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        self.edges = []
        
    def addEdge(self, e): # addEdge(self, FlowEdge(v,w,capacity))
        self.adj[e.v].append(e)
        self.adj[e.w].append(e)
        self.adj.edges.append(e)
        self.E += 1
        
    def __str__(self): # 모든 정방향 간선 출력
        edge = []
        for v in range(self.V):
            for e in self.adj[v]:
                if v == e.v: edge.append(f"{e}\n")
        return "".join(edge)
            
    def copy(self):
        newFlowNetwork = FlowNetwork(self.V)
        for e in self.edges:
            newFlowNetwork.addEdge(FlowEdge(e.v, e.w, e.capacity))