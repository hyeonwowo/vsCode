import sys

def linear(lin,b):
    c = lin
    b = b - 1
    for cnt in range(b):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    c[i][j] += (c[i][k] * lin[k][j]) // 1000
    return c

if __name__ == "__main__":
    n, b = map(int, sys.stdin.readline().split())
    lin = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    result = linear(lin, b)
    for row in result:
        print(*row)