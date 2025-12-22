import sys

def backtracking():
    if len(path) == 4:
        print(*path)
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                path.append(i+1)
                backtracking()
                path.pop()
                visited[i] = False

if __name__ == "__main__":
    N = 4
    path = []
    visited = [False] * N
    backtracking()