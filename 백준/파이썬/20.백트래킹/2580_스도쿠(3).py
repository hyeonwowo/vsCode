import sys # 개선사항 반영한 최종본

def sudoku(cnt):
    if cnt == zerocnt:
        for row in board:
            print(*row) 
        sys.exit(0)
    else:
        i,j = zeropoint[cnt]
        if board[i][j] == 0:
            numlst = findnum(i,j)
            for element in numlst:
                board[i][j] = element
                sudoku(cnt+1)
                board[i][j] = 0

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
                zeropoint.append((i,j))
    print()
    sudoku(0)