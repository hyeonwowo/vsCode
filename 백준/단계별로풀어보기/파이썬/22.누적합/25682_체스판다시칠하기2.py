import sys

def prefix_sum(chessboard):
    pass

def chess(board):
    count = 0
    return count

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    chessboard = [list(sys.stdin.readline().strip()) for _ in range(n)]
    chessboard.insert(0,[0]*m)
    for i in range(n+1):
        chessboard[i].insert(0,0) # 1부터 인덱싱 처리하면 됨