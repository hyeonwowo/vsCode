import sys # 개선사항 필요(오류수정, 시간단축)

def sudoku(cnt):
    if cnt == zerocnt:
        for row in board:
            print(*row) 
        sys.exit(0)
    else:
        for i in range(9): # 각 sudoku() 메서드마다 이중포문 발생 -> 시간 지연
            for j in range(9):
            # x, y = zeropoint[cnt] 인덱싱 접근 처리로 시간 개선
                if board[i][j] == 0:
                    numlst = findnum(i,j)
                    for element in numlst:
                        board[i][j] = element
                        sudoku(cnt+1)
                        # 되돌리는 로직 추가
                        board[i][j] = 0 # 백트래킹에 있어 필수적
                        
def findnum(x,y): # 찾기
    numlst = set([1,2,3,4,5,6,7,8,9])
    for k in range(9):
        a, b = board[x][k], board[k][y]
        numlst.discard(a)
        numlst.discard(b)
    
    a, b = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            numlst.discard(board[a+i][b+j])
            
    return numlst

if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    zerocnt = 0
    zeropoint = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0: 
                zerocnt += 1
                # 0 인 좌표 저장
                zeropoint.append((i,j))
    print()
    sudoku(0)