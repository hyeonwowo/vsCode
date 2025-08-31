import sys
import copy
sys.setrecursionlimit(10**6)

def left(lst):
    res = []
    i = 0
    while i < len(lst):
        if i+1 < len(lst) and lst[i] == lst[i+1]:
            res.append(lst[i]+lst[i+1])
            i += 2
        else:
            res.append(lst[i])
            i += 1
    # 길이가 n보다 짧으면 0 채우기
    while len(res) < n:
        res.append(0)
    return res

def right(lst):
    lst.reverse()
    res = left(lst)
    res.reverse()
    return res

def up(lst):
    res = left(lst)
    return res

def down(lst):
    lst.reverse()
    res = left(lst)
    res.reverse()
    return res

def moveblock(dx, dy, board):
    if dy == 0:
        res = []
        for i in range(n):
            row = [board[i][j] for j in range(n) if board[i][j] != 0]
            if dx == -1:
                newrow = left(row)
            else:
                newrow = right(row)
            res.append(newrow)
        return res
    
    else:  
        res = [[0]*n for _ in range(n)]
        for j in range(n):
            col = [board[i][j] for i in range(n) if board[i][j] != 0]
            if dy == -1:
                newcol = down(col)
            else:
                newcol = up(col)
            for i in range(n):
                res[i][j] = newcol[i]
        return res

def backtracking(cnt, board):
    global maxval
    if cnt == 5:
        for row in board:
            for element in row:
                maxval = max(maxval, element)
        return
    else:
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            copyboard = copy.deepcopy(board)
            moveboard = moveblock(dx, dy, copyboard)
            backtracking(cnt+1, moveboard)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    maxval = 0
    backtracking(0, grid)
    print(maxval)
