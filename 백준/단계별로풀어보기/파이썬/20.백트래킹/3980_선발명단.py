import sys 

def makeTeam(i):
    global maxval
    if i == 11:
        total = 0
        for i, j in path:
            total += grid[i][j]
        maxval = max(maxval, total)
        return
    else:
        for j in range(11):
            if not visited[i] and grid[i][j] != 0:
                path.append((i, j))
                makeTeam(i+1)
                path.pop()

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        grid = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
        ovlPoint = []
        for i in range(11):
            for j in range(11):
                if grid[i][j] != 0:
                    ovlPoint.append((i, j))
                    
        path = []
        visited = [False] * 11
        maxval = 0
        makeTeam(0)
        
        print(maxval)