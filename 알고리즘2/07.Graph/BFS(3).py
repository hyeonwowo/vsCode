# 강의자료 BFS
from queue import Queue

class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        
    def put(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
        
    def BFS(self, s):
        self.s = s
        self.visited = [False for _ in range(self.V)] # [False] * self.V 로 대체가능
        self.fromVertex = [None for _ in range(self.V)] # [None] * self.V 로 대체가능
        self.distance = [None for _ in range(self.V)] # [-1] * self.V 로 대체가능
        
        queue = Queue()
        queue.put(s)
        
        self.visited[s] = True
        self.fromVertex[s] = None
        self.distance[s] = 0
        
        while not queue.empty():
            current_vertex = queue.get()
            for neighbor in self.adj[current_vertex]:
                if self.visited[neighbor] == False:
                    queue.put(neighbor)
                    self.visited[neighbor] = True
                    self.fromVertex[neighbor] = current_vertex
                    self.distance[neighbor] = self.distance[current_vertex] + 1
        
        print(self.visited)
        print(self.fromVertex)
        print(self.distance)
    
# 그래프 생성
g = Graph(6)
g.put(0, 1)
g.put(1, 2)
g.put(1, 3)
g.put(1, 5)
g.put(2, 4)
g.put(4, 5)

g.BFS(0)  # BFS 실행