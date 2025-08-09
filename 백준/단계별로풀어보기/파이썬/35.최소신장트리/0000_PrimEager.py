import heapq

def prim_eager(V, adj):
    mst = []
    total_weight = 0
    dist = [float('inf')] * V
    parent = [-1] * V
    visited = [False] * V

    dist[0] = 0
    heap = [(0, 0)]  # (weight, vertex)

    while heap:
        weight, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        if parent[u] != -1:
            mst.append((parent[u], u, weight))
        for v, w in adj[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                parent[v] = u
                heapq.heappush(heap, (w, v))

    return total_weight, mst


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        # 0-based 변환
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))

    total_weight, mst = prim_eager(V, adj)

    print(total_weight)
    for u, v, w in mst:
        print(u + 1, v + 1, w)  # 다시 1-based로 출력
