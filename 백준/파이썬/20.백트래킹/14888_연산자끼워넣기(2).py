import sys

def backtrack(depth,total,plus,minus,mul,div):
    global maxcnt
    global mincnt
    if depth == N:
        maxcnt = max(total,maxcnt)
        mincnt = min(total,mincnt)
        return
    
    if plus:
        backtrack(depth+1,total+num[depth],op[0]-1,op[2],op[3],op[4])
    if minus:
        backtrack(depth+1,total-num[depth],op[0],op[2]-1,op[3],op[4])
    if mul:
        backtrack(depth+1,total*num[depth],op[0],op[2],op[3]-1,op[4])
    if div:
        if total < 0:
            backtrack(depth+1,-(-total//num[depth]),op[0],op[2],op[3],op[4]-1)
        else:
            backtrack(depth+1,total//num[depth],op[0],op[2],op[3],op[4]-1)
            

    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    op = list(map(int, sys.stdin.readline().split()))
    
    maxcnt = -float('inf')
    mincnt = float('inf')
    backtrack(0,num[0],op[0],op[1],op[2],op[3])
    print(maxcnt)
    print(mincnt)