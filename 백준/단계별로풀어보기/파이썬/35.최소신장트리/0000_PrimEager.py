def prim_eager(V, adj):
    import heapq

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
