import sys
sys.setrecursionlimit(10**6)

def TP(V, adj):
    def recur(v):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                recur(w)
        reverselst.append(v)
        
    reverselst = []
    visited = [False] * V
    for v in range(V):
        if not visited[v]:
            recur(v)
            
    reverselst.reverse()
    return reverselst

def SCC(V, adj, tporder):
    def recur(v, comp):
        visited[v] = True
        comp.append(v)
        for w in adj[v]:
            if not visited[w]:
                recur(w, comp)
        
    visited = [False] * V
    sccList = []
    for v in tporder:
        if not visited[v]:
            comp = []
            recur(v, comp)
            sccList.append(comp)
    return sccList

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    res = []
    for _ in range(T):
        n = int(sys.stdin.readline())
        lst = list(map(int, sys.stdin.readline().split()))
        
        adj = [[] for _ in range(n)]
        adj_rev = [[] for _ in range(n)]
        
        for i in range(n):
            v, w = i, lst[i]-1 # 0-based index 영점 조절
            adj[v].append(w)
            adj_rev[w].append(v)
            
        tporder = TP(n, adj_rev)
        sccs = SCC(n, adj, tporder)
        
        team_cnt = 0
        for comp in sccs:
            if len(comp) > 1:
                team_cnt += len(comp)
                
        res.append(n-team_cnt)
        
    print(res,sep='\n')
    