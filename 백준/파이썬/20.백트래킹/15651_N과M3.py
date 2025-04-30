N,M = map(int,input().split())
path = [] 
visited = [False] * (N+1)

def backtrack():
    if len(path) == M:
        print(*path)
        return
    else:
        for i in range(1,N+1):
            if not visited[i]:
                path.append(i)
                backtrack()
                path.pop()
                
if __name__ == "__main__":
    backtrack()