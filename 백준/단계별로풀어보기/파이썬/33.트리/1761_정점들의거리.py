# LCS2 알고리즘 + weight 합산

import sys
from collections import deque

def LCS(a, b):
    pass

def BFS():
    pass

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    adj = [[] for _ in range(N+1)]
    for _ in range(N+1):
        v, w, weight = map(int, sys.stdin.readline().split())
    
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())
        
        
    