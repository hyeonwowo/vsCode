import sys

def linear(lin):
    n = len(lin)
    c = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += lin[i][k] * lin[k][j]
    return c

def power(a, n):
    if n == 0:
        return 1
    
    half = power(a, n // 2)
    if half % 2 == 0:
        power(half * half, n // 2)
    else:
        power(half * half * a, n // 2)

if __name__ == "__main__":
    n, b = map(int, sys.stdin.readline().split())
    lin = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    result = power(linear(lin, b),n)
    for row in result:
        print(*row)