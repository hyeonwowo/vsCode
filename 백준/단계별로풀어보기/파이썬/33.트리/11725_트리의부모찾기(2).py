import sys
from collections import deque
sys.setrecursionlimit(10**6)

def BFS(start):
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for w in adjTree[node]:
            if not parent[w]:
                parent[w] = node
                queue.append(w)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    adjTree = [[] for _ in range(n+1)]
    parent = [0] * (n+1)
    
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        adjTree[a].append(b)
        adjTree[b].append(a)
    
    BFS(1)
    for i in range(2, n+1):
        print(parent[i])