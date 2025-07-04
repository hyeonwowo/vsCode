import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, V, E):
        self.v = V
        self.e = E
        self.adj = [[] for _ in range(V+1)]
        self.visited = [0] * (V+1)  # 방문 순서 기록
        self.order = 1              # 방문 순서 카운터

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def DFS(self, S):
        def recur(v):
            self.visited[v] = self.order
            for w in sorted(self.adj[v]):  # 오름차순 방문
                if self.visited[w] == 0:
                    self.order += 1
                    recur(w)
        recur(S)

if __name__ == "__main__":
    input = sys.stdin.readline
    V, E, S = map(int, input().split())

    g = Graph(V, E)
    for _ in range(E):
        v, w = map(int, input().split())
        g.addEdge(v, w)

    g.DFS(S)

    for i in range(1, V+1):
        print(g.visited[i])
