import sys # kruskal
import math

class UF:
    def __init__(self, V):
        self.parent = [i for i in range(V)]
        self.size = [1] * V
        
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        if roota == rootb:
            return False
        if self.size[roota] < self.size[rootb]:
            self.parent[roota] = rootb
            self.size[rootb] += self.size[roota]
        else:
            self.parent[rootb] = roota
            self.size[roota] += self.size[rootb]

def kruskal(V, edges):
    edges.sort()
    
    uf = UF(V)
    total_weight = 0
    
    for weight, v, w in edges:
        if uf.union(v, w):
            total_weight += weight

    return total_weight

def distance(x1, y1, x2, y2):
    dx, dy = (x1-x2), (y1-y2)
    return math.sqrt(dx*dx + dy*dy)

if __name__ == "__main__":
    V = int(sys.stdin.readline())
    
    vertexPoint = []
    for _ in range(V):
        x, y = map(float, sys.stdin.readline().split())
        vertexPoint.append((x, y))
        
    edges = []
    for i in range(V):
        for j in range(i+1, V):
            weight = distance(vertexPoint[i][0], vertexPoint[i][1], vertexPoint[j][0], vertexPoint[j][1])
            edges.append((weight, i, j))
            
    total_weight = kruskal(V, edges)
    print(total_weight)
        