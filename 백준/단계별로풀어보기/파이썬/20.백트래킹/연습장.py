import sys
input = sys.stdin.readline

def backtracking(start, depth):
    if depth == m:
        print(*path)
        return

    prev = 0
    for i in range(start, n):
        if lst[i] != prev:
            path.append(lst[i])
            prev = lst[i]
            backtracking(i, depth + 1)  # i부터 시작 → 비내림차순 유지
            path.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = sorted(map(int, input().split()))

    path = []
    backtracking(0, 0)
