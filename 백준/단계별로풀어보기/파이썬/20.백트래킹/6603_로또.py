import sys

def backtracking(start):
    if len(path) == m:
        print(*path)
        return
    else:
        for i in range(start, len(lst)):
            if not visited[i]:
                visited[i] = True
                path.append(lst[i])
                backtracking(i)
                visited[i] = False
                path.pop()

if __name__ == "__main__":
    query = []
    m = 6
    
    while True:
        inputlst = list(map(int, sys.stdin.readline().split()))
        if inputlst[0] == 0:
            break
        query.append(inputlst[1:])
        
    for lst in query:
        visited = [False] * len(lst)
        path = []
        backtracking(0)
        print()