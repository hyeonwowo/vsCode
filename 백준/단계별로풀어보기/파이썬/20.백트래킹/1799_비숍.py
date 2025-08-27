import sys
sys.setrecursionlimit(10000)

def backtracking(idx, cnt, color):
    global maxcnt
    if idx == len(pos[color]):
        maxcnt[color] = max(maxcnt[color], cnt)
        return
    
    x, y = pos[color][idx]
    if not left_diag[x+y] and not right_diag[x-y+n-1]:
        left_diag[x+y] = right_diag[x-y+n-1] = True # +n-1은 음수보정
        backtracking(idx+1, cnt+1, color)
        left_diag[x+y] = right_diag[x-y+n-1] = False
    
    backtracking(idx+1, cnt, color)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    pos = [[], []]  # 흑칸 / 백칸 후보 위치
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 놓을 수 있는 자리
                pos[(i+j)%2].append((i, j))
    
    # 체스판에 좌표 x, y가 있을 때
    left_diag = [False] * (2*n) # \ 방향 대각선
    right_diag = [False] * (2*n) # / 방향 대각선
    maxcnt = [0, 0]
    
    backtracking(0, 0, 0)  # 흑칸 탐색
    backtracking(0, 0, 1)  # 백칸 탐색
    
    print(maxcnt[0] + maxcnt[1])
