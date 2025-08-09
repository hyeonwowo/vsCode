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

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return total_weight, mst

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))  # (가중치, 정점1, 정점2)

    total_weight, mst = kruskal(V, edges)

    print(total_weight)
    for u, v, w in mst:
        print(u, v, w)
