import sys

def reverse_buckets(n, m):
    buckets = list(range(1, n + 1))
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        buckets[i - 1:j] = reversed(buckets[i - 1:j])
    return buckets

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    print(*reverse_buckets(n, m))
