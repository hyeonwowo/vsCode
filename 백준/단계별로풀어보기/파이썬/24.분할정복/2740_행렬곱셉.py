import sys

def mullinear(a, b):
    c = [[0]*R for _ in range(N)]
    for i in range(N):
        for j in range(R):
            for k in range(K):
                c[i][j] += a[i][k] * b[k][j]
    return c


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    alinear = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    K2, R = map(int, sys.stdin.readline().split())
    blinear = [list(map(int, sys.stdin.readline().split())) for _ in range(K2)]
    
    result = mullinear(alinear, blinear)
    for row in result:
        print(*row)
