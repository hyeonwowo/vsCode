from pathlib import Path
from queue import PriorityQueue
from queue import Queue
import timeit

class DirectedEdge: # 방향 가중치 간선 클래스
    def __init__(self, v, w, weight):
        self.v, self.w, self.weight = v, w, weight
    def __lt__(self, other):
        assert(isinstance(other, DirectedEdge))
        return self.weight < other.weight
    def __gt__(self, other):
        assert(isinstance(other, DirectedEdge))
        return self.weight > other.weight
    def __eq__(self, other):
        if other == None: return False
        assert(isinstance(other, DirectedEdge))
        return self.v == other.v and self.w == other.w and self.weight == other.weight
    def __str__(self):
        return f"{self.v}---{self.weight}---{self.w}"
    def __repr__(self):
        return self.__str__()
    
class EdgeWeightedDigraph:         
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(g.V)]
        self.edges = []
    
    def addEdge(self, v, w, weight):
        e = DirectedEdge(v, w, weight)
        self.adj[v].append(e)
        self.edges.append(e)
        self.E += 1
        
    def outDegree(self, v):
        return len(self.adj[v])
    
    def __str__(self):
        rtList = [f"{self.V} verrtices and {self.E} edges\n"]
        for v in range(self.V):
            for e in self.adj[v]: rtList.append(f"{e}\n")
        return "".join(rtList)
    
    def negate(self):
        g = EdgeWeightedDigraph(self.V)
        for e in self.edges: g.addEdge(e.v, e.w, -e.weight)
        return g

    def reverse(self):
        g = EdgeWeightedDigraph(self.V)
        for e in self.edges: g.addEdge(e.w, e.v, e.weight)
        return g
    
    @staticmethod
    def fromFile(fileName):
        filePath = Path(__file__).with_name(fileName)   # Use the location of the current .py file   
        with filePath.open('r') as f:
            phase = 0
            line = f.readline().strip() # Read a line, while removing preceding and trailing whitespaces
            while line:                                
                if len(line) > 0:
                    if phase == 0: # Read V, the number of vertices
                        g = EdgeWeightedDigraph(int(line))
                        phase = 1
                    elif phase == 1: # Read edges
                        edge = line.split()
                        if len(edge) != 3: raise Exception(f"Invalid edge format found in {line}")
                        g.addEdge(int(edge[0]), int(edge[1]), float(edge[2]))                        
                line = f.readline().strip()
        return g
    
class IndexMinPQ:
    def __init__(self, maxN):
        if maxN < 0: raise Exception("maxN < 0")
        self.maxN = maxN
        self.n = 0
        self.keys = [None] * (maxN+1)
        self.pq = [-1] * (maxN+1)
        self.pq = [-1] * maxN
        
    def isEmpty(self):
        return self.n == 0
    
    def contains(self, i):
        self.vaildateIndex(i)
        return self.pq[i] != -1
    
    def vaildateIndex(self, i):
        if i<0: raise Exception(f"index {i} < 0")
        if i>=self.maxN: raise Exception(f"index {i} > {self.maxN}")
    
    
def topologicalSortWithCycleDetection(g):
    
class SP:
   
class DijkstraSP(SP):
           
class AcyclicSP(SP):
                            
class BellmanFordSP(SP):
        
if __name__ == "__main__":
    e1 = DirectedEdge(2, 3, 0.1)
    e1a = DirectedEdge(2, 3, 0.1)
    e2 = DirectedEdge(3, 4, 0.9)
    e3 = DirectedEdge(7, 3, 0.2)
    print("e1, e1a, e2, e3", e1, e1a, e2, e3)
    print("e1 == e1a", e1 == e1a)
    print("e1 < e2", e1 < e2)
    print("e1 > e3", e1 > e3)
    print("e2 < e3", e2 < e3)
    print()

    g1 = EdgeWeightedDigraph(8)
    g1.addEdge(4, 5, 0.35)
    g1.addEdge(5, 4, 0.35)
    g1.addEdge(4, 7, 0.37)
    g1.addEdge(5, 7, 0.28)
    g1.addEdge(7, 5, 0.28)
    g1.addEdge(5, 1, 0.32)
    g1.addEdge(0, 4, 0.38)
    g1.addEdge(0, 2, 0.26)
    g1.addEdge(7, 3, 0.39)
    g1.addEdge(1, 3, 0.29)
    g1.addEdge(2, 7, 0.34)
    g1.addEdge(6, 2, 0.40)
    g1.addEdge(3, 6, 0.52)
    g1.addEdge(6, 0, 0.58)
    g1.addEdge(6, 4, 0.93)
    print(g1)
    print(g1.adj[0])       
    print(g1.adj[7])
    print()

    g8i = EdgeWeightedDigraph.fromFile("wdigraph8i.txt")
    print("g8i", g8i)
    print("dijkstraSP on g8i")
    sp8i = DijkstraSP(g8i, 0)
    for i in range(g8i.V):
        if sp8i.hasPathTo(i): print(i, sp8i.distTo[i], sp8i.pathTo(i))
        else: print(i, "no path exists")
    print()

    g8a = EdgeWeightedDigraph.fromFile("wdigraph8a.txt")    
    print("g8a", g8a)
    print("dijkstraSP on g8a")
    sp8a = DijkstraSP(g8a, 0)
    print(sp8a.distTo)
    print(sp8a.edgeTo)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    print("BellmanFordSP on g8a")
    sp8a = BellmanFordSP(g8a, 0)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    print("acyclicSP on g8a")
    sp8a = AcyclicSP(g8a, 4)
    print(sp8a.distTo)
    print(sp8a.edgeTo)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    g8bn = EdgeWeightedDigraph.fromFile("wdigraph8b.txt").negate()
    print("acyclicSP on -g8b for vertex 5 as the source to find longest paths")
    sp8bn = AcyclicSP(g8bn, 5)
    for i in range(g8bn.V):
        if sp8bn.hasPathTo(i): print(i, -sp8bn.distTo[i], sp8bn.pathTo(i))
        else: print(i, "no path exists")    
    print()
    
    g6n = EdgeWeightedDigraph.fromFile("wdigraph6n.txt")
    print("BellmanFordSP on g6n")
    sp6n = BellmanFordSP(g6n, 0)
    for i in range(g6n.V):
        if sp6n.hasPathTo(i): print(i, sp6n.distTo[i], sp6n.pathTo(i))
        else: print(i, "no path exists")    
    print()

    print("DijkstraSP on g6n")
    sp6nD = DijkstraSP(g6n, 0)
    for i in range(g6n.V):
        if sp6nD.hasPathTo(i): print(i, sp6nD.distTo[i], sp6nD.pathTo(i))
        else: print(i, "no path exists")    
    print()
