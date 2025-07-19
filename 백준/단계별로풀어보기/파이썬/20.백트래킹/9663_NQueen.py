import sys

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): # 대각선 구하기 로직. 대각선 - (t,t)(-t,t)(-t,-t)(t,-t)
            return False
    return True

def n_queens(x): # x는 몇번째 queen을 둘 차례인지 나타냄
    global ans # 함수 바깥에서 선언한 ans를 사용하기 위해 global 선언
    if x == n:
        ans += 1
        return
    else:
        for i in range(n): # n개의 체스말을 놓으니 n번 반복
            # [x, i]에 퀸을 놓겠다.
            row[x] = i # row[x] = i는 for문 안에서 매번 i를 바꿈. (첫번재 반복 - 1번째에 배치, 두번재 반복 - 2번재에 배치 .. )
            if is_promising(x):
                n_queens(x+1)
                
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ans = 0
    row = [0] * n
    n_queens(0)
    print(ans)