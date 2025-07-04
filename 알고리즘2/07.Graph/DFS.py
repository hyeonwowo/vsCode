class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]

    def put(self, v, w): # 무방향그래프
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def DFS(self, v):
        visited = []  # 탐색한 노드를 저장하는 집합
        def recur(node):
            if node not in visited:  # 방문하지 않은 노드만 탐색
                visited.append(node)
                for neighbor in self.adj[node]:
                    recur(neighbor)

        recur(v)
        return visited  # set을 list로 변환하여 반환

if __name__ == "__main__":
    # 그래프 생성
    g = Graph(6)
    g.put(0, 1)
    g.put(1, 2)
    g.put(1, 3)
    g.put(1, 5)
    g.put(2, 4)
    g.put(4, 5)
    
    print(g.DFS(0))  # DFS 실행