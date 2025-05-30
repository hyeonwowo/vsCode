import sys
# 문제점1) 최소값 비교하지 않고 바로 덮어쓰고 있음 -> minovr = min(minovr, abs(..))
# 문제점2) visited[i] = True/False 처리를 해주지 않음 -> vistied[i] = Ture/False
# 문제점3) 답은 맞지만, 시간초과
def backtracking(k):
    global minovr
    if k == N//2:
        linkteam = [i for i in range(N) if i not in startteam]
        minovr = min(minovr, abs(calteamovr(startteam) - calteamovr(linkteam)))
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                startteam.append(i)
                backtracking(k+1)
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
    backtracking(0)
    print(minovr)