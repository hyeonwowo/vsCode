import sys
import heapq

def prim_eager(V, adj):
    mst = []
    total_weight = 0

    dist = [float('inf')] * V          # 각 정점을 MST에 붙이는 최소비용(key)
    parent = [-1] * V         # MST 복원용
    visited = [False] * V

    # 시작 정점: 0
    dist[0] = 0
    heap = [(0, 0)]           # (key, v)

    while heap:
        key, v = heapq.heappop(heap) # key : 현재 Mst 정점 집합에서 정점v로 가는 간선의 최소 가중치
        if visited[v]:
            continue
        visited[v] = True

        total_weight += key
        if parent[v] != -1: # 시작 정점은 부모가 없으니 제외, 그 외에는 방금 선택된 간선을 MST에 기록
            mst.append((parent[v], v, key))  # parent[v], v = mst에 속한 정점, mst 바깥에 속한 정점

        # v의 이웃을 살피며 dist 갱신 (decrease-key 효과)
        for w, weight in adj[v]:
            if not visited[w] and weight < dist[w]:
                dist[w] = weight # w를 트리에 붙이는 현재 최저비용 갱신
                parent[w] = v # 그 비용을 만들어 준 부모는 v
                heapq.heappush(heap, (weight, w)) # 새 key로 힙에 등록

    return total_weight, mst


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(V)]
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        adj[v].append((w, weight))
        adj[w].append((v, weight))

    total_weight, mst = prim_eager(V, adj)

    for v, w, weight in mst:
        print(v, w, weight)
    print(total_weight)
