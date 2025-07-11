import sys

class Edge:
    pass

class Graph:
    pass

def dijkstra():
    pass

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n, m, t = map(int, sys.stdin.readline().split())
        
        dest = []
        for _ in range(t):
            dest.append(int(sys.stdin.readline()))
    