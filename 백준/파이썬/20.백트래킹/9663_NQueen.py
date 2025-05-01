import sys

def backtracking(k): # 매개인자 - 행
    global cnt
    for i in range(N): # 열 번호를 순회
        if queen(k,i): # k번째 행, i번째 열. queen() 검사를 통과하면, k번째행의 i번째 열에 queen 배치
            board[k] = i
            if k == N-1: # 전체 queen의 수가 N-1개라면(0~N-1) cnt리턴
                cnt += 1 # cnt는, 여러곳에서 호출된 함수 backtracking의 이곳저곳에서 동시에 다뤄짐
                return
            else:
                backtracking(k+1) # 아니라면 다음행으로 이동

def queen(a,b): # a : 현재 놓으려는 퀸의 "행" 번호. b : 현재 놓으려는 퀸의 "열" 번호
    for i in range(a):
        if board[i] == b or abs(board[i]-b) == abs(i-a): # 대각선 위치의 열에서 현재 퀸의 열을 뺀 값과 대각선 위치의 행에서 현재 퀸의 행을 뺀 값의 절댓값이 같다
            # board[k] = i 는 k번째 행에 i열에 퀸을 놓았다는 뜻. 즉 board[0] = 1 이면, 0행 1열에 퀸이 있다는 뜻
            return False
    return True

if __name__ == "__main__":
    N = int(sys.stdin.readline()) 
    board = [0]*N
    cnt = 0
    backtracking(0) # 0번째 행에서 퀸을 놓을 열을 하나씩 시도
    print(cnt)    