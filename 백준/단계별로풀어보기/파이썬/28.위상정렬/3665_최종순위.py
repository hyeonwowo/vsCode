import sys

class Graph:
    def __init__(self, V, E):
        pass
    
    def addEdge(self, v, w):
        pass
    
    def DFS(self, S):
        pass
    
if __name__ == "__main__":
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        team = list(map(int, sys.stdin.readline().split()))
        teamchange = int(sys.stdin.readline())
        
        for _ in range(teamchange):
            v, w = map(int, sys.stdin.readline().split())
            