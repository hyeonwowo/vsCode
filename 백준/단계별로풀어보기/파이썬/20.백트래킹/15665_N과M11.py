import sys

def backtracking():
    if len(path) == m:
        print(*path)
        return 
    else:
        prev = 0
        for i in range(n):
            if prev != lst[i]:
                prev = lst[i]
                path.append(lst[i])
                backtracking()
                path.pop()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = sorted(list(map(int, sys.stdin.readline().split())))
    
    path = []
    backtracking()
    