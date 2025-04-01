import sys

def reverseBucket(N,M):
    arr = [i+1 for i in range(N)]
    for _ in range(M):
        copy = []
        j = 0
        x, y = map(int, sys.stdin.readline().split())
        x = x-1
        copy = arr[x:y]
        copy.reverse()
        
        for i in range(x,y):
            arr[i] = copy[j]
            j += 1
    
    return arr

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    result = reverseBucket(N,M)
    print(*result)