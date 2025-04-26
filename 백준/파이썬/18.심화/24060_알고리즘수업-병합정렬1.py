import sys
sys.setrecursionlimit(10**6)

def merge_sort(A, tmp, p, r):
    global count, result
    if p < r:
        q = (p + r) // 2
        merge_sort(A, tmp, p, q)
        merge_sort(A, tmp, q + 1, r)
        merge(A, tmp, p, q, r)

def merge(A, tmp, p, q, r):
    global count, result, K
    i, j, t = p, q + 1, p   
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
    
    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1
    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1
        
    for i in range(p, r + 1):
        A[i] = tmp[i]
        count += 1
        if count == K:
            result = A[i]

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    tmp = [0] * (N+1)
    count = 0
    result = -1
    
    merge_sort(A, tmp, 0, N-1)
    print(result)
