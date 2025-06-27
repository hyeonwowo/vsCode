import sys
from collections import deque

def BFS(S):
    visited = [False for _ in range(MAX)]
    depth = [0 for _ in range(MAX)]
    
    queue = deque([S])
    while queue:
        node = queue.popleft()
        if node == k:
            return depth[node]
        for neighbor in (node + 1, node - 1, node * 2):
            if 0 <= neighbor < MAX and visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1 
        
if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    MAX = k * 3
    print(BFS(n))