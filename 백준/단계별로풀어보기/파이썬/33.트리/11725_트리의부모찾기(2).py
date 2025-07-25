import sys
from collections import deque
sys.setrecursionlimit(10**6)

def BFS():
    pass

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    adjTree = [[] for _ in range(n+1)]
    parent = [0] * (n+1)
    