import sys

def backtracking():
    if len(path) == M:
        print(*path)
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                path.append(Nnum[i])
                backtracking()
                path.pop()
                visited[i] = False

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    Nnum = sorted(map(int, sys.stdin.readline().split()))
    visited = [False] * N
    path = []
    backtracking()