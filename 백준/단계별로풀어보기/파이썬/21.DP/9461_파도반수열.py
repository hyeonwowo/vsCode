import sys

def triangle(n): # 그냥 기본적인 구조를 외우는게 나을듯 (메모이제이션-DP)
    if board[n] != -1: # 해당하는 삼각형 존재시
        return board[n] # 삼각형 값 리턴
    board[n] = triangle(n-3) + triangle(n-2) # 없으면 계산 (재귀형태) + board배열에 적용
    return board[n] # 리턴해주는 이유 (재귀로 들어온 triangle(n-k)의 값을 적용해주기 위해)

if __name__ == "__main__":
    board = [-1 for _ in range(101)] # -1 로 초기화 (append)하는 방법보다 처음부터 초기화한 후 연산하는게 효과적인듯
    board[1], board[2], board[3] = 1, 1, 1
    
    n = int(sys.stdin.readline())
    result = []
    for _ in range(n):
        k = int(sys.stdin.readline())
        result.append(triangle(k))
    print('\n'.join(map(str,result)))
