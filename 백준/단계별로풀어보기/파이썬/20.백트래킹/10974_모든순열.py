import sys

def backtracking(start):
    if len(path) == n:
        print(*path)
        return
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                path.append(i)
                backtracking(i+1)
                path.pop()
                visited[i] = False
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    visited = [False] * (n+1)
    path = []
    start = 0
    
    backtracking(start)