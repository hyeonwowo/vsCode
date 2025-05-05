import sys

def nqueen(k):
    global cnt
    if k == N:
        cnt += 1
        return
    else:
        for i in range(N):
            if isqueen(k,i):
                board[k] = i
                nqueen(k+1)

def isqueen(a,b):
    for i in range(a):
        if board[i] == b or abs(board[i]-b) == abs(i-a):
            return False
    return True

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    cnt = 0
    board = [0] * N
    nqueen(0)
    print(cnt)
    