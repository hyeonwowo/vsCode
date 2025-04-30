import sys

def backtrack(k):
    global cnt
    for i in range(N):
        if queen(k,i):
            board[k] = i
            if k == N-1:
                cnt += 1
                return
            else:
                backtrack(k+1)

def queen(a,b):
    for i in range(a):
        if board[i] == b or abs(board[i]-b) == abs(i-a):
            return False
    return True

if __name__ == "__main__":
    N = int(input())
    board = [0] * N
    cnt = 0
    backtrack(0)
    print(cnt)