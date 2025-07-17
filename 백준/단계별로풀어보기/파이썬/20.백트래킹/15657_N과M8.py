import sys

path = []
def backtracking(start, m):
    if len(path) == m:
        print(*path)
        return
    else:
        for i in range(start, n):
            path.append(lst[i])
            backtracking(i, m)
            path.pop()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    
    backtracking(0, m)