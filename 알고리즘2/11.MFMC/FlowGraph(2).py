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
