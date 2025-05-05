import sys
input = sys.stdin.readline

def backtrack(depth):
    if depth == M:
        print(*path)
        return
    for i in range(1, N + 1):
        path.append(i)
        backtrack(depth + 1)
        path.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    path = []
    backtrack(0)
