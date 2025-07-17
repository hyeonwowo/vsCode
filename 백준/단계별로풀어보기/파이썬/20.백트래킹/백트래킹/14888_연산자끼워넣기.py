import sys

def backtrack(depth, total, plus, minus, multiply, divide):
    global mincnt
    global maxcnt
    
    if depth == N:
        maxcnt = max(total, maxcnt)
        mincnt = min(total, mincnt)
        return
    
    # if문이 여러개라 하나에 걸리면 backtrack() 다음으로 넘어가는게 아니라, plus에서도 실행, minus에서도 실행, .. 조건에 성립하면 모든 if문을 작동시켜서 트리처럼
    if plus:
        backtrack(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        backtrack(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        backtrack(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        if total < 0:
            backtrack(depth + 1, -(-total // num[depth]), plus, minus, multiply, divide - 1)
        else:
            backtrack(depth + 1, total // num[depth], plus, minus, multiply, divide - 1)

if __name__ == "__main__":
    mincnt = float('inf')
    maxcnt = -float('inf') 
    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    op = list(map(int, sys.stdin.readline().split()))

    backtrack(1, num[0], op[0], op[1], op[2], op[3])
    print(maxcnt)
    print(mincnt)
