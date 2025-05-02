import sys

def backtracking():
    if len(path) == M:
        print(*path)
        return
    else:
        for i in range(1,N+1):
            path.append(i)
            backtracking()
            path.pop()

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    path = []
    backtracking()