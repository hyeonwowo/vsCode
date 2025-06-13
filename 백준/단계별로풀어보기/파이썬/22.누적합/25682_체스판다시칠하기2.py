import sys

def chessboard(board,k):
    startwhiteboard = color("W",board)
    startblackboard = color("B",board)
    
    prefix_startwhiteboard = totalsum(startwhiteboard)
    prefix_startblackboard = totalsum(startblackboard)
    
    prefixlst = []
    for i in range(k, n+1):
        for j in range(k, m+1):
            prefixlst.append(rangetotalsum(prefix_startblackboard,i,j))
            prefixlst.append(rangetotalsum(prefix_startwhiteboard,i,j))
    return min(prefixlst)

def color(start,board):
    resultboard = [[0] * (n+1) for _ in range(m+1)]
    for i in range(n):
        for j in range(m):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                if board[i][j] != start:
                    resultboard[i][j] = 1
            else:
                if board[i][j] == start:
                    resultboard[i][j] = 1
    return resultboard

def totalsum(arr):
    prefix = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + arr[i][j]
    return prefix

def rangetotalsum(prefix,i,j):
    return prefix[i][j] - prefix[i][j-k] - prefix[i-k][j] + prefix[i-k][j-k]    

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    board = [[0] + list(sys.stdin.readline().strip()) for _ in range(m)]
    board.insert(0,[0]*(m+1))
    print(chessboard(board, k))