from queue import Queue

class Graph:
    def __init__(self, V):  
        self.V = V 
        self.E = 0 
        self.adj = [[] for _ in range(V)]   

    def addEdge(self, v, w): 
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for w in self.adj[v]:
                if v <= w: rtList.append(f"{v}-{w}\n")
        return "".join(rtList)

class DFS:
    def __init__(self, g, s): 
        def recur(v):        
            self.visited[v] = True            
            for w in g.adj[v]:
                if not self.visited[w]: 
                    recur(w)
                    self.fromVertex[w] = v
        assert(isinstance(g, Graph) and s >= 0 and s < g.V)
        self.g, self.s = g, s
        self.visited = [False for _ in range(g.V)]
        self.fromVertex = [None for _ in range(g.V)]
        recur(s)        

    def pathTo(self, v):
        if not self.visited[v]: return None
        path = []
        while v != self.s:
            path.append(v)
            v = self.fromVertex[v]
        path.append(self.s)
        path.reverse()
        return path

    def hasPathTo(self, v):
        return self.visited[v]

class BFS:
    def __init__(self, g, s):        
        assert(isinstance(g, Graph) and s >= 0 and s < g.V)
        self.g, self.s = g, s
        self.visited = [False for _ in range(g.V)]
        self.fromVertex = [None for _ in range(g.V)]
        self.distance = [None for _ in range(g.V)]
        queue = Queue()
        queue.put(s)        
        self.visited[s] = True
        self.distance[s] = 0
        while queue.qsize() > 0:        
            v = queue.get()            
            for w in g.adj[v]:
                if not self.visited[w]:
                    queue.put(w)                    
                    self.visited[w] = True
                    self.fromVertex[w] = v
                    self.distance[w] = self.distance[v] + 1

    def pathTo(self, v):
        if not self.visited[v]: return None
        path = []
        while v != self.s:
            path.append(v)
            v = self.fromVertex[v]
        path.append(self.s)
        path.reverse()
        return path

    def hasPathTo(self, v):
        return self.visited[v]

    def distTo(self, v):
        return self.distance[v]

class CC:
    def __init__(self, g):
        def recur(v):        
            self.id[v] = self.count
            for w in g.adj[v]:
                if self.id[w] < 0: 
                    recur(w)                            
        self.g = g
        self.id = [-1 for i in range(g.V)]
        self.count = 0 
        for v in range(g.V):
            if self.id[v] < 0:
                recur(v)
                self.count += 1        

    def connected(self, v, w):
        return self.id[v] == self.id[w]

if __name__ == "__main__":   
    g = Graph(13)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 5)
    g.addEdge(0, 6)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(7, 8)
    g.addEdge(9, 10)
    g.addEdge(9, 11)
    g.addEdge(9, 12)
    g.addEdge(11, 12)

    print(g)
    
    print(g.adj[0], g.degree(0))    
    print(g.adj[5], g.degree(5))
    print(g.adj[9], g.degree(9))
    
    dfs = DFS(g,0)
    print(dfs.visited, dfs.fromVertex)
    print(dfs.pathTo(0))
    print(dfs.pathTo(1))
    print(dfs.pathTo(2))
    print(dfs.pathTo(3))
    print(dfs.pathTo(4))
    print(dfs.pathTo(5))
    print(dfs.pathTo(6))
    print(dfs.pathTo(7))
    print(dfs.hasPathTo(6))
    print(dfs.hasPathTo(7))

    bfs = BFS(g,0)
    print(bfs.visited, bfs.fromVertex)
    print(bfs.pathTo(0), bfs.distTo(0))
    print(bfs.pathTo(1), bfs.distTo(1))
    print(bfs.pathTo(2), bfs.distTo(2))
    print(bfs.pathTo(3), bfs.distTo(3))
    print(bfs.pathTo(4), bfs.distTo(4))
    print(bfs.pathTo(5), bfs.distTo(5))
    print(bfs.pathTo(6), bfs.distTo(6))
    print(bfs.pathTo(7), bfs.distTo(7))
    print(dfs.hasPathTo(6))
    print(dfs.hasPathTo(7))

    cc = CC(g)
    print(cc.count, cc.id)
    print(cc.connected(0, 3))
    print(cc.connected(0, 7))
    print(cc.connected(0, 9))
    print(cc.connected(7, 8))
    print(cc.connected(7, 11))
    print(cc.connected(10, 12))