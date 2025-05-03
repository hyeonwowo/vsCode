import sys

def find_candidates(x, y):
    used = set()
    # 행, 열
    for i in range(9):
        used.add(board[x][i])
        used.add(board[i][y])
    # 3x3 사각형
    sx, sy = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            used.add(board[sx + i][sy + j])
    return [num for num in range(1, 10) if num not in used]

def solve(k):
    if k == len(blank):
        for row in board:
            print(*row)
        sys.exit(0)  # 정답 하나만 출력하고 종료
    x, y = blank[k]
    for cand in find_candidates(x, y):
        board[x][y] = cand
        solve(k + 1)
        board[x][y] = 0  # backtrack

if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    blank = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    solve(0)
