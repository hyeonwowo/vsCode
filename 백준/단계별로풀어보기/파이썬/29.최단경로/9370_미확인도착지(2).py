import sys
import heapq

def dijkstra(start):
    dist = [int(1e9)] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if dist[u] < d:
            continue
        for v, w in G[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, K = map(int, sys.stdin.readline().split())
        s, g, h = map(int, sys.stdin.readline().split())
        
        G = [[] for _ in range(N + 1)]
        gh_weight = None
        
        for _ in range(M):
            u, v, w = map(int, sys.stdin.readline().split())
            G[u].append((v, w))
            G[v].append((u, w))
            if (u == g and v == h) or (u == h and v == g):
                gh_weight = w
        
        candidates = [int(sys.stdin.readline()) for _ in range(K)]

        dist_s = dijkstra(s)
        dist_g = dijkstra(g)
        dist_h = dijkstra(h)

        result = []
        for x in candidates:
            # 경로 1: s -> g -> h -> x
            # 경로 2: s -> h -> g -> x
            path1 = dist_s[g] + gh_weight + dist_h[x]
            path2 = dist_s[h] + gh_weight + dist_g[x]
            if dist_s[x] == path1 or dist_s[x] == path2:
                result.append(x)

        result.sort()
        print(' '.join(map(str, result)))
