import sys

def floyd_warshall(n, dist):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())

    INF = float('inf')
    dist = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dist[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)  # ✅ 여러 간선 중 최소 비용만 저장

    floyd_warshall(n, dist)

    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            if dist[i][j] == INF:
                row.append("0")
            else:
                row.append(str(dist[i][j]))
        print(" ".join(row))
