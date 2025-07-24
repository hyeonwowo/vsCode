import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    dp = [[float('inf')] * k for _ in range(n)]
    coin = list(map(int, sys.stdin.readline().split()))
                
    for i in range(k):
        for j in range(n):
            pass
             
            
                