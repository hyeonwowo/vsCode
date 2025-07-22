import sys # 안겹치게 각 포지션별 선수 선택
           # 시간복잡도가 너무 오래걸림..
           # 오버롤이 있는 좌표를 저장해서 하나씩 돌아볼까?
def makeTeam(start):
    global maxval
    if start == 11:
        total = 0
        for i in range(11):
            for j in range(11):
                if grid[i][j] == 0:
                    return
                total += grid[i][j]
        maxval = max(maxval, total)
        return
    else:
        for i in range(start, 11):
            if not visited[i]:
                visited[i] = True
                path.append(i)
                makeTeam(i+1)
                path.pop()
                visited[i] = False

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