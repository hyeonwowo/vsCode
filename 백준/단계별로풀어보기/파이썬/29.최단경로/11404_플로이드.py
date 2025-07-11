import sys

def floyd_warshall(V, adj):
    dist = [[float('inf')] * (V+1) for _ in range(V+1)]
    
    for i in range(1, V+1):
        dist[i][i] = 0
        
    for v in range(1, V+1):
        for w, weight in adj[v]:
            dist[v][w] = min(dist[v][w], weight)  # ✅ 여러 간선 중 최소값 사용
            # 동일한 정점쌍 (v, w)에 대해 여러 간선이 존재 할 수 있기 때문에 min() 사용. ex) 1, 2, 3 / 1, 2, 1
    
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    adj = [[] for _ in range(V+1)]
    
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        adj[v].append((w, weight))
        
    dist = floyd_warshall(V, adj)
    
    for i in range(1 ,V+1):
        for j in range(1, V+1):
            print(0 if dist[i][j] == float('inf') else dist[i][j], end=" ")  # ✅ inf → 0
        print()
