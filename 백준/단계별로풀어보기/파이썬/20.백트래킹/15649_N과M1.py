import sys

N,M = map(int, sys.stdin.readline().split())
visited = [False] * (N+1)
path = []

def backtrack():
    if len(path) == M:
        print(*path)
        return
    for i in range(1,N+1):
        if not visited[i]:
            path.append(i)
            visited[i] = True
            backtrack()
            path.pop()
            visited[i] = False
        
backtrack()