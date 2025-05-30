import sys

def backtracking():
    if len(path) == M:
        print(*path)
        return
    else:
        for i in range(1,N+1):
            if not visited[i]:
                visited[i] = True
                path.append(i)
                backtracking()
                path.pop()
                visited[i] = False

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    path = []
    visited = [False] * (N+1)
    backtracking()