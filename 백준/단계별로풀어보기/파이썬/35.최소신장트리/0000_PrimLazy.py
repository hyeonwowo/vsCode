import heapq

def prim_lazy(V, adj):
    visited = [False] * V
    mst = []
    total_weight = 0
    min_heap = []

    def visit(u):
        visited[u] = True
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, u, v))

    visit(0)  # 시작 정점
    while min_heap and len(mst) < V - 1:
        weight, u, v = heapq.heappop(min_heap)
        if visited[v]:
            continue
        mst.append((u, v, weight))
        total_weight += weight
        visit(v)

    return total_weight, mst

