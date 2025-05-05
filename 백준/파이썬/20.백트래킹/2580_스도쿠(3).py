import sys

def sudoku(idx):
    # ✅ 개선 1: 모든 빈칸을 미리 리스트로 저장하고, 그 인덱스를 따라가며 채움
    # 기존 코드에서는 매번 9x9를 돌면서 0을 찾았지만, 이 방식은 한 번만 찾고 끝남
    if idx == len(zero_positions):  # 모든 빈칸을 채웠다면
        for row in board:
            print(*row)
        sys.exit(0)  # ✅ 개선 2: 첫 정답에서 바로 종료 (기존과 동일)
    
    x, y = zero_positions[idx]  # 미리 저장된 빈칸 좌표를 가져옴
    for num in findnum(x, y):  # 현재 위치에 넣을 수 있는 수들을 하나씩 시도
        board[x][y] = num
        sudoku(idx + 1)  # 다음 빈칸으로
        board[x][y] = 0  # 백트래킹: 원상 복구

def findnum(x, y):
    candidates = set(range(1, 10))  # ✅ 개선 3: set(range(1, 10)) 으로 더 간결하게 만듦

    # 행, 열에서 숫자 제거
    for k in range(9):
        candidates.discard(board[x][k])
        candidates.discard(board[k][y])
    
    # 3x3 박스 내 숫자 제거
    box_x, box_y = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            candidates.discard(board[box_x + i][box_y + j])

    return candidates  # 남은 수가 현재 칸에 들어갈 수 있는 후보 숫자

if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    # ✅ 개선 4: 빈칸 좌표들을 미리 리스트에 저장하여 재탐색 제거
    zero_positions = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

    sudoku(0)  # idx = 0부터 시작 (zero_positions의 0번째 좌표부터 채우기)
