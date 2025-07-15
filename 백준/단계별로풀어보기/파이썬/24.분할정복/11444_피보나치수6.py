import sys

MOD = 1000000007

def mat_mult(a, b):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD],
    ]

def mat_pow(matrix, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = mat_mult(result, matrix)
        matrix = mat_mult(matrix, matrix)
        n //= 2
    return result

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
    else:
        base = [[1, 1], [1, 0]]
        fib_matrix = mat_pow(base, n - 1)
        print(fib_matrix[0][0])  # == F(n)
