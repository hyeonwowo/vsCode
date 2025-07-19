import sys # 기존 제출 3796ms -> 3028ms

def numCand(x, y):
    numst = set()
    
    for i in range(9):
        numst.add(board[x][i])
        numst.add(board[i][y])
        
    tx, ty = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            numst.add(board[tx + i][ty + j])
    
    stst = set([1,2,3,4,5,6,7,8,9])
    return sorted(stst - numst)

def sudoku(currcnt):
    if currcnt == zerocnt:
        return [row[:] for row in board]
    else:
        zerox, zeroy = zeropoint[currcnt]
        numcandidate = numCand(zerox, zeroy)
        
        for num in numcandidate:
            board[zerox][zeroy] = num
            result = sudoku(currcnt+1)
            if result:
                return result
            board[zerox][zeroy] = 0
    return None            

if __name__ == "__main__":
    board = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]
    zeropoint = []
    zerocnt = 0
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                zeropoint.append((i,j))
                zerocnt += 1
                
    res = sudoku(0)
    
    for row in res:
        print(*row, sep='')