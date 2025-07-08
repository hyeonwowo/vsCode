import sys # 다익스트라, 벨만 - 한지점에서 모든지점
           # 플로이드 - 모든지점에서 모든지점

def floyd_warshall(V, adj):
    # 거리 배열 초기화
    dist = [[float('inf')] * (V + 1) for _ in range(V + 1)]

    # 자기 자신까지의 거리는 0
    for i in range(1, V + 1):
        dist[i][i] = 0

    # 인접 행렬 정보로 거리 초기화
    for u in range(1, V + 1):
        for v, weight in adj[u]:
            dist[u][v] = weight

    # 핵심 로직: 점화식 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for k in range(1, V + 1):        # 경유 노드
        for i in range(1, V + 1):    # 출발 노드
            for j in range(1, V + 1):# 도착 노드
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))  # 방향 그래프

    dist = floyd_warshall(V, adj)

    # 출력 (1-based index)
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if dist[i][j] == float('inf'):
                print("INF", end=' ')
            else:
                print(dist[i][j], end=' ')
        print()
