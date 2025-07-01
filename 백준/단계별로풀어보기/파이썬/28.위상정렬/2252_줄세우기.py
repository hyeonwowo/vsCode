import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, V, E):
        self.v = V
        self.e = E
        self.adj = [[] for _ in range(V+1)]
        self.visited = [False] * (V+1)
        self.result = []
        
    def addEdge(self, v, w):
        self.adj[v].append(w)
        
    def DFS(self, S):
        def recur(v):
            pass
        recur(S)
        self.visited[S] = True
        self.result.append(S)
        
    def tpsort(self, result):
        return result

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    