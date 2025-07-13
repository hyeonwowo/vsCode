import sys

def power(a, n):
    if n == 0:
        return 1
    else:
        half = power(a, n // 2)
        if n % 2 == 0:
            return (half * half) % C
        else:
            return (half * half * a) % C

if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())
    print(power(A, B))