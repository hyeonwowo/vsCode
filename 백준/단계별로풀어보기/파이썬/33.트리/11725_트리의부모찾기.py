import sys # DFS 풀이
sys.setrecursionlimit(10**6)

def dfs(start):
    def recur(v):
        for w in adjTree[v]:
            if not parent[w]:
                parent[w] = v
                recur(w)
    recur(start)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    adjTree = [[] for _ in range(n+1)]
    parent = [0] * (n+1)
    
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        adjTree[a].append(b)
        adjTree[b].append(a)
        
    dfs(1)
    
    for i in range(2, n+1):
        print(parent[i])