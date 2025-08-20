import sys # kruskal 1660ms

class UF:
    def __init__(self, V):
        self.parent = [i for i in range(V+1)]
        self.size = [1] * (V+1)
        
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
            self.size[rootb] += roota
        else:
            self.parent[rootb] = roota
            self.size[roota] += rootb
        return True
    
def kruskal(V, edges):
    edges.sort()
    
    uf = UF(V)
    total_weight = 0
    cnt = 0
    for weight, v, w in edges:
        if uf.union(v, w):
            total_weight += weight
            cnt += 1
    
    if cnt != V-1:
        return -1
    else:
        return total_weight

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    weightsum = 0
    edges = []
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        weightsum += weight
        edges.append((weight, v, w))
    
    
    total_weight = kruskal(V, edges)
    if total_weight == -1:
        print(-1)
    else:
        print(weightsum - total_weight)