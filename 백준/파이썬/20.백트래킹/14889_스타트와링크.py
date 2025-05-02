import sys

def backtrack(index, team):
    global minscore
    if len(team) == N//2:
        other_team = [i for i in range(N) if i not in team]
        start = teamscore(team)
        link = teamscore(other_team)
        minscore = min(minscore, abs(start-link))
        if minscore == 0:
            print(0)
            sys.exit(0)
        return
    
    for i in range(index, N):
        team.append(i)
        backtrack(i+1,team)
        team.pop()

def teamscore(team): # 4, 6, 7...
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a = team[i]
            b = team[j]
            score += ovr[a][b] + ovr[b][a]
    return score

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    ovr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    startteam = [False] * N
    minscore = float('inf')
    backtrack(0,[])
    print(minscore)