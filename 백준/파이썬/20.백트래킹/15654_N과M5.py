import sys

def backtracking():
    if len(path) == M:
        print(*path)
        return
    else:
        pass

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    Nnum = sorted(list(map(int, sys.stdin.readline().split())))
    
    path = []
    backtracking()