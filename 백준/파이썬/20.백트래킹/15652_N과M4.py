import sys

N,M = map(int, sys.stdin.readline().split())

path = []

def backtrack(start):
    if len(path) == M:
        print(*path)
        return
    else:
        for i in range(start, N+1):
            path.append(i)
            backtrack(i)
            path.pop()

if __name__ == "__main__":
    backtrack(1)