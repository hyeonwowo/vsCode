import sys 

def makeTeam(i, total):
    global maxval
    if i == 11:
        maxval = max(maxval, total)
        return
    else:
        for j in range(11):
            if not visited[j] and grid[i][j] != 0:
                visited[j] = True
                makeTeam(i+1, total+grid[i][j])
                visited[j] = False

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        grid = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
        visited = [False] * 11
        maxval = 0
        makeTeam(0,0)
        
        print(maxval)