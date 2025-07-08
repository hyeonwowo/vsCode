import sys # BFS 이용
from collections import deque

def BFS():
    depth = {}
    visited = {}
    depth[start] = 0
    visited[start] = True
    
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            return depth[node]
        else:
            for w in (node-1, node+1, node*2):
                if 0 <= w <= 1000000:
                    if w not in visited.keys(): # visited -> visited.keys()
                        visited[w] = True
                        if w == node * 2:
                            depth[w] = depth[node]
                            queue.appendleft(w) # queue.append() -> queue.appendleft
                        else:
                            depth[w] = depth[node] + 1
                            queue.append(w)
                        
    return None
if __name__ == "__main__":
    start, end = map(int, sys.stdin.readline().split())
    print(BFS())