import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    global cnt
    visited[v] = 1  # 방문 중
    next_v = graph[v]

    if visited[next_v] == 0:  # 아직 방문하지 않은 경우
        dfs(next_v)
    elif visited[next_v] == 1:  # 방문 중인 노드를 다시 만남 → 사이클 발견
        cur = next_v
        cycle_size = 1
        while cur != v:  # v까지 돌아올 때까지 카운트
            cur = graph[cur]
            cycle_size += 1
        cnt += cycle_size

    visited[v] = 2  # 방문 완료

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        lst = [0] + list(map(int, sys.stdin.readline().split()))  # 1-indexed
        graph = lst
        visited = [0] * (n + 1)
        cnt = 0  # 사이클에 포함되는 학생 수

        for i in range(1, n + 1):
            if visited[i] == 0:
                dfs(i)

        print(n - cnt)  # 팀을 못 이룬 학생 수
