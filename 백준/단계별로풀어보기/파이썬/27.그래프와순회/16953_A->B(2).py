import sys # 메모리 터짐 [] 대신에 set(), dict{} 사용
from collections import deque 

MAX = 20001
def BFS():
    visited = set()
    depth = dict()
    
    queue = deque([start])
    visited.add(start)
    depth[start] = 1 # 요구사항에 따라 0으로 조절
    
    while queue:
        node = queue.popleft()
        if node == end:
            return depth[node]
        else:
            for neighbor in (node * 2, int(str(node)+"1")):
                if neighbor <= end * 2:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            depth[neighbor] = depth[node] + 1
                            queue.append(neighbor)
    return -1

if __name__ == "__main__":
    start, end = map(int, sys.stdin.readline().split())
    print(BFS())