import sys

def power(a, n):
    if n == 0:
        return 1
    else:
        half = power(a, n // 2)
        if n % 2 == 0:
            return (half * half) % c
        else:
            return (half * half * a) % c

if __name__ == "__main__":
    a, n, c = map(int, sys.stdin.readline().split())
    print(power(a, n))