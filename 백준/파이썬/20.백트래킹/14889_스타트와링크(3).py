import sys
# 시간초과 발생 -> 중복되는 조합 제거 [1,2] [2,1] 과 같은 경우 : start 변수 사용
def backtracking(k,start):
    global minovr
    if k == N//2:
        linkteam = [i for i in range(N) if i not in startteam]
        minovr = min(minovr, abs(calteamovr(startteam) - calteamovr(linkteam)))
        if minovr == 0:
            print(0)
            sys.exit(0)
        return
    else:
        for i in range(start,N):
            if not visited[i]:
                visited[i] = True
                startteam.append(i)
                backtracking(k+1,i+1)
                startteam.pop()
                visited[i] = False
    
def calteamovr(team):
    result = 0
    for i in range(N//2):
        for j in range(N//2):
            if i<j:
                a, b = team[i], team[j]
                result += (ovr[a][b] + ovr[b][a])
    return result

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    ovr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [False] * N
    startteam = []
    minovr = float('inf')
    backtracking(0,0)
    print(minovr)