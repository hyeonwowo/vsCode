import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 경로 압축
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False
        self.parent[rootB] = rootA
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
        v, w, weight = map(int, input().split())
        edges.append((weight, v, w))  # (가중치, 정점1, 정점2)


    total_weight, mst = kruskal(V, edges)

    for v, w, weight in mst:
        print(v, w, weight)
    print(total_weight)