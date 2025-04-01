import sys

def changeBucket(N,M):
    arr = [i+1 for i in range(N)]
    
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
        x, y = x-1, y-1
        arr[x], arr[y] = arr[y], arr[x]
    return arr

N, M = map(int, sys.stdin.readline().split())
result = changeBucket(N,M)
print(*result)