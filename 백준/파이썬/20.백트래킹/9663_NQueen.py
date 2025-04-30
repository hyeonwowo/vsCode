import sys

def backtracking(k):
    global cnt
    for i in range(N):
        if queen(k,i): # k번째 행, i번째 열
            board[k] = i
            if k == N-1:
                cnt += 1
                return
            else:
                backtracking(k+1)

def queen(a,b):
    for i in range(a):
        if board[i] == b or abs(board[i]-b) == abs(i-a): # 대각선 위치의 열에서 현재 퀸의 열을 뺀 값과 대각선 위치의 행에서 현재 퀸의 행을 뺀 값의 절댓값이 같다
            return False
    return True

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [0]*N
    cnt = 0
    backtracking(0)
    print(cnt)    