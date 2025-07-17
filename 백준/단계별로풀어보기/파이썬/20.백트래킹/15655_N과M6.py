import sys

def backtracking(start):
    if len(path) == m:
        print(*path)
        return
    else:
        for i in range(start, n):
            if not visited[i]:
                visited[i] = True
                path.append(lst[i])
                backtracking(i)
                path.pop()
                visited[i] = False

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    
    path = []
    visited = [False] * n
    backtracking(0)