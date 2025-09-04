import sys
sys.setrecursionlimit(10**6)

def has_cycle_dfs(v, adj, visited, rec_stack):
    visited[v] = True # 방문 여부
    rec_stack[v] = True # 현재 DFS 경로(재귀스택) 포함 여부
    
    for w in adj[v]:
        if not visited[w]:  # 아직 방문하지 않은 경우
            if has_cycle_dfs(w, adj, visited, rec_stack):
                return True
        elif rec_stack[w]:  # 이미 현재 경로에 있는 노드를 다시 방문 → 사이클 존재
            return True
    
    rec_stack[v] = False  # DFS 경로에서 제거
    return False

def detect_cycle(V, adj):
    visited = [False] * V
    rec_stack = [False] * V
    
    for v in range(V):
        if not visited[v]:
            if has_cycle_dfs(v, adj, visited, rec_stack):
                return True
    return False

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(V)]
    
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)  # 방향 그래프 (u → v)
    
    if detect_cycle(V, adj):
        print("Cycle detected")
    else:
        print("No cycle")
