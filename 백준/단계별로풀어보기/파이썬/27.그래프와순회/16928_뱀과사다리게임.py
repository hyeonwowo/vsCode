import sys
from collections import deque

def BFS():
    queue = deque([1])
    visited = [False] * 101
    depth = [0] * 101
    
    visited[1] = True
    depth[1] = 0
    
    while queue:
        node = queue.popleft()
        if node == 100:
            return depth[node]
        
        for spot in range(node + 1, node + 7):
            if spot <= 100 and not visited[spot]:
                # 사다리 또는 뱀이 있는 경우 도착 지점으로 이동
                if spot in ladders:
                    dest = ladders[spot]
                elif spot in snakes:
                    dest = snakes[spot]
                else:
                    dest = spot
                
                if not visited[dest]:
                    queue.append(dest)
                    visited[dest] = True
                    depth[dest] = depth[node] + 1

if __name__ == "__main__":
    l, s = map(int, sys.stdin.readline().split())
    
    ladders = dict() # 딕셔너리로 하는게 효과적
    snakes = dict()
    
    for _ in range(l):
        v, w = map(int, sys.stdin.readline().split())
        ladders[v] = w  # 사다리: 시작 v -> 도착 w

    for _ in range(s):
        v, w = map(int, sys.stdin.readline().split())
        snakes[v] = w  # 뱀: 시작 v -> 도착 w

    print(BFS())
