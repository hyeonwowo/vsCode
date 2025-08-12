import sys # kruskal

class UF:
    def __init__(self, V):
        self.parent = [i for i in range(V)]
        self.size = [1] * V
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
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

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    edges = []
    
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        edges.append((weight, v, w))