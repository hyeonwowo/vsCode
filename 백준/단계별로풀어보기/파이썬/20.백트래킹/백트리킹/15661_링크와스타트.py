import sys

def backtracking(k, start, team_size):
    global minovr
    if k == team_size:
        linkteam = [i for i in range(N) if not visited[i]]
        startovr = calteamovr(startteam)
        linkovr = calteamovr(linkteam)
        minovr = min(minovr, abs(startovr - linkovr))
        if minovr == 0:
            print(0)
            sys.exit(0)
        return
    
    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            startteam.append(i)
            backtracking(k + 1, i + 1, team_size)
            startteam.pop()
            visited[i] = False

def calteamovr(team):
    result = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a, b = team[i], team[j]
            result += ovr[a][b] + ovr[b][a]
    return result

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    ovr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    minovr = float('inf')

    # 가능한 팀 크기: 1명 ~ N//2명
    for team_size in range(1, N // 2 + 1):
        visited = [False] * N
        startteam = []
        backtracking(0, 0, team_size)

    print(minovr)
