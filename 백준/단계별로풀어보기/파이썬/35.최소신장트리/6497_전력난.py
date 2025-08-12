import sys  # kruskal

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
        return True

def kruskal(V, edges):
    edges.sort()
    uf = UF(V)
    total_weight = 0
    for weight, v, w in edges:
        if uf.union(v, w):
            total_weight += weight
    return total_weight

if __name__ == "__main__":
    while True:
        line = sys.stdin.readline().split()
        if not line:
            break
        V, E = map(int, line)
        if V == 0 and E == 0:
            break

        edges = []
        sum_weight = 0
        for _ in range(E):
            v, w, weight = map(int, sys.stdin.readline().split())
            edges.append((weight, v, w))
            sum_weight += weight

        res = kruskal(V, edges)
        print(sum_weight - res)
