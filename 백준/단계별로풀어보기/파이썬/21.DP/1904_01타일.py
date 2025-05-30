import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [-1] * (N+1)
    board[0],board[1] = 1,1
    
    for i in range(2,N+1):
        board[i] = board[i-2] + board[i-1]

    print(board[N]%15746)