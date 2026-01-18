import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

LENGTH = 21  # 2^20 > 100000

def dfs(v, depth):
    visited[v] = True
    d[v] = depth

    for w, cost in graph[v]:
        if visited[w]:
            continue
        parent[w][0] = v
        wdp[w] = wdp[v] + cost
        dfs(w, depth + 1)

def set_parent():
    dfs(1, 0)
    for i in range(1, LENGTH):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a

    # 깊이 맞추기
    for i in range(LENGTH - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    # 공통 조상 직전까지 올리기
    for i in range(LENGTH - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


if __name__ == "__main__":
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    parent = [[0] * LENGTH for _ in range(n + 1)]
    visited = [False] * (n + 1)
    d = [0] * (n + 1)     # depth
    wdp = [0] * (n + 1)   # root(1)부터 누적 거리

    for _ in range(n - 1):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    set_parent()

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        c = lca(a, b)
        print(wdp[a] + wdp[b] - 2 * wdp[c])
