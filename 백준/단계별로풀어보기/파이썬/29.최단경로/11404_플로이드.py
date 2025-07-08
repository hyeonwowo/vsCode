import sys

def floyd_warshall(V, adj):
    dist = [[float('inf')] * (V+1) for _ in range(V+1)]
    
    for i in range(1, V+1):
        dist[i][i] = 0
        
    for v in range(1, V+1):
        for w, weight in adj[v]:
            dist[v][w] = weight
            
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(V+1)]
    
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        adj[v].append((w, weight))
        
    dist = floyd_warshall(V, adj)
    
    for row in dist:
        print(*row)