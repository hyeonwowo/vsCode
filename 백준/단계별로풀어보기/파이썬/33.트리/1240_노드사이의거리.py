import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v, target, dist):
    if v == target:
        return dist
    visited[v] = True

    for nxt, w in adj[v]:
        if not visited[nxt]:
            result = dfs(nxt, target, dist + w)
            if result != -1: # 가는 경로가 있고 if v == target: 에서 경로길이를 반환하면
                return result # 해당 경로 리턴
    return -1 # 해당하는 경로가 없을때 return -1

if __name__ == "__main__":
    N, M = map(int, input().split())

    adj = [[] for _ in range(N+1)]

    for _ in range(N-1):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))
        adj[b].append((a, w))

    for _ in range(M):
        x, y = map(int, input().split())
        visited = [False] * (N+1)
        print(dfs(x, y, 0))
