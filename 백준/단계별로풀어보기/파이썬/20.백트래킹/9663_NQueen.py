import sys

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): # 대각선 구하기 로직. 대각선 - (t,t)(-t,t)(-t,-t)(t,-t)
            return False
    return True

def n_queens(x):
    global ans # 
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)
                
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ans = 0
    row = [0] * n
    n_queens(0)
    print(ans)

