import sys

def fill_buckets(n, m):
    buckets = [0] * n
    for _ in range(m):
        i, j, k = map(int, sys.stdin.readline().split())
        buckets[i-1:j] = [k] * (j - i + 1)
    return buckets

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    print(*fill_buckets(n, m))
