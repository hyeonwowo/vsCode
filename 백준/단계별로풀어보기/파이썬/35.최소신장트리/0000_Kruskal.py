import sys

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return False
        if self.size[roota] < self.size[rootb]:
            self.parent[roota] = rootb
            self.size[rootb] += self.size[roota]
        else:
            self.parent[rootb] = roota
            self.size[roota] += self.size[rootb]
        return True

def kruskal(V, edges):
    edges.sort()
    uf = UnionFind(V)

    mst = []
    total_weight = 0
    
    for weight, v, w in edges:
        if uf.union(v, w):
            mst.append((v, w, weight))
            total_weight += weight
    
    return total_weight, mst

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    edges = []
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        edges.append((weight, v, w))
        
    total_weight, mst = kruskal(V, edges)
    
    for v, w, weight in mst:
        print(v, w, weight)
    print(total_weight)