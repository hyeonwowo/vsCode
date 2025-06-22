class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        
    def put(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
        
    def BFS(self, start):
        visited = []
        queue = [start]
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend(self.adj[node]) # 인접 노드들을 "한번에" queue에 추가하기 위해 extend 사용 -> 이미 방문한 노드가 들어가지만 visited로 나중에 처리함
        
        return visited
    
if __name__ == "__main__":
    # 그래프 생성
    g = Graph(6)
    g.put(0, 1)
    g.put(1, 2)
    g.put(1, 3)
    g.put(1, 5)
    g.put(2, 4)
    g.put(4, 5)

    print(g.BFS(0))  # BFS 실행