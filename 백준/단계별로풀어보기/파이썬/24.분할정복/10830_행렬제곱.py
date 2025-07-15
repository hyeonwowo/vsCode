import sys
sys.setrecursionlimit(10**6)

def linear(alin, blin):
    c = [[0] * T for _ in range(T)]
    for i in range(T):
        for j in range(T):
            for k in range(T):
                c[i][j] += alin[i][k] * blin[k][j]
                c[i][j] %= 1000
    return c

def power(lst, n):
    if n == 0:
        return [[1 if i == j else 0 for j in range(T)] for i in range(T)] # 항등행렬 초기화 (대각선 1, 나머지 0) 어떤 행렬과 곱해도 그 행렬 유지
    
    half = power(lst, n // 2)
    if n % 2 == 0:
        return linear(half, half)
    else:
        return linear(linear(half, half), lst)

if __name__ == "__main__":
    T, N = map(int, sys.stdin.readline().split())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
    res = power(lst, N)
    for row in res:
        print(*row)
