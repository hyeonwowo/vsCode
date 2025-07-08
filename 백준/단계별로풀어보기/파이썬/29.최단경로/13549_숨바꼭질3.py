import sys
import heapq

def dijkstra(start, end):
    max_limit = 1000000
    distTo = [float('inf')] * (max_limit + 1)
    visited = [False] * (max_limit + 1)

    distTo[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True

        for w in (v * 2, v - 1, v + 1):
            if 0 <= w <= max_limit:
                cost = 0 if w == v * 2 else 1
                if distTo[w] > distTo[v] + cost:
                    distTo[w] = distTo[v] + cost
                    heapq.heappush(pq, (distTo[w], w))

    return distTo[end]

if __name__ == "__main__":
    start, end = map(int, sys.stdin.readline().split())
    print(dijkstra(start, end))
