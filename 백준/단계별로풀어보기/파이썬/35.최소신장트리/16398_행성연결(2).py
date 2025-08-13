import sys # 1240ms

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
            self.parent[roota] = self.parent[rootb]
            self.size[rootb] += self.size[roota]
        else:
            self.parent[rootb] = self.parent[roota]
            self.size[roota] += self.size[rootb]
        return True
    
def kruskal(n, edges):
    edges.sort()
    uf = UF(n)
    total_weight = 0
    
    for weight, v, w in edges:
        if uf.union(v, w):
            total_weight += weight
    
    return total_weight
            
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    edges = []
    for i in range(1, n):
        for j in range(i):
            w = grid[i][j]
            edges.append((w, i, j))
            
    total_weight = kruskal(n, edges)
    print(total_weight)