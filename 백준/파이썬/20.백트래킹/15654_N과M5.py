import sys

def backtracking():
    if len(path) == M:
        print(*path)
        return
    else:
        for element in Nnum:
            if not vistied[element]:
                vistied[element] = True
                path.append(element)
                backtracking()
                path.pop()
                vistied[element] = False

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    Nnum = sorted(list(map(int, sys.stdin.readline().split())))
    
    path = []
    vistied = [False] * (max(Nnum)+1)
    backtracking()