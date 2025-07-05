import sys # 메모리 터짐 [] 대신에 set(), dict{} 사용해보자
from collections import deque 

MAX = 20001
def BFS():
    visited = [False] * (end + MAX)
    depth = [0] * (end + MAX)
    
    queue = deque([start])
    visited[start] = True
    depth[start] = 1
    
    while queue:
        node = queue.popleft()
        if node == end:
            return depth[node]
        else:
            visited[node] = True
            for neighbor in (node * 2, int(str(node)+"1")):
                if 1 <= neighbor <= end+MAX:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            depth[neighbor] = depth[node] + 1
                            queue.append(neighbor)
    return -1

if __name__ == "__main__":
    start, end = map(int, sys.stdin.readline().split())
    print(BFS())