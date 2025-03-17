class SCC:
    def __init__(self, g): # Do strongly-connected-components pre-processing, based on Kosaraju-Sharir algorithm
        reverseGraph = g.reverse()
        tpList = topologicalSort(reverseGraph)
        self.count = 0
        self.id = [-1 for _ in range(g.V)]
        visited = [False for _ in range(g.V)]
        visitedFrom = [None for _ in range(g.V)]
        
        def recur(v):
            visited[v] = True
            for w in g.adj[v]:
                if not visited[w]:
                    recur(w)
                    visitedFrom[w] = v
            
        for v in tpList:
            recur(v)
            if self.id[v] < 0:
                recur(v)
                count += 1
        

    def connected(self, v, w): # Are v and w connected?
        return self.id[v] == self.id[w]