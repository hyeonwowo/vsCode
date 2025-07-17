import sys

def backtracking():
    if len(path) == m:
        print(*path)
        return
    else:
        for i in range(n):
            path.append(lst[i])
            backtracking()
            path.pop()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    path = []
    backtracking()