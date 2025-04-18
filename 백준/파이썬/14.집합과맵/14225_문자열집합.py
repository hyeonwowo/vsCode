import sys

def count_common(n, m):
    s = {sys.stdin.readline().strip() for _ in range(n)}  # 집합 S
    count = 0
    for _ in range(m):
        word = sys.stdin.readline().strip()
        if word in s:
            count += 1
    return count

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    print(count_common(n, m))
