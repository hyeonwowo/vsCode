import sys

def findcandidate(x, y):
    rowcand = set()
    colcand = set()
    sqcand = set()
    
    for i in range(9):
        rowcand.add(board[x][i])
        colcand.add(board[i][y])

    tx, ty = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            sqcand.add(board[tx + i][ty + j])
    
    used = rowcand | colcand | sqcand 
    return list(numset - used)

def sudoku(current):
    if current == cnt:
        # 정답 보드를 깊은 복사로 반환
        return [row[:] for row in board]

    i, j = zeropoint[current]
    numlst = findcandidate(i, j)

    for element in numlst:
        board[i][j] = element # 원본 리스트 변경
        result = sudoku(current + 1)
        if result:
            return result  # 정답 찾으면 바로 상위로 반환
        board[i][j] = 0  # 백트래킹
    
    return None  # 모든 후보 실패 시

if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    zeropoint = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    cnt = len(zeropoint)
    numset = set(range(1, 10))

    res = sudoku(0)
    
    for row in res:
        print(*row)
