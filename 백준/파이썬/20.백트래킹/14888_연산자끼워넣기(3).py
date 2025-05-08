import sys

def backtracking(opcnt,total,add,minus,mul,div):
    global minval
    global maxval
    if opcnt == N-1:
        maxval = max(maxval, total)
        minval = min(minval, total)
        return
    else:
        if add:
            backtracking(opcnt+1,total+numlst[opcnt+1],op[0]-1,op[1],op[2],op[3])
        if minus:
            backtracking(opcnt+1,total-numlst[opcnt+1],op[0],op[1]-1,op[2],op[3])
        if mul:
            backtracking(opcnt+1,total*numlst[opcnt+1],op[0],op[1],op[2]-1,op[3])
        if div:
            if total > 0:
                backtracking(opcnt+1,total//numlst[opcnt+1],op[0],op[1],op[2],op[3]-1)
            else: 
                backtracking(opcnt+1,-(-total//numlst[opcnt+1]),op[0],op[1],op[2],op[3]-1)
                
    
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numlst = list(map(int, sys.stdin.readline().split()))
    op = list(map(int, sys.stdin.readline().split()))
    minval = float('inf')
    maxval = -float('inf')
    
    backtracking(0,numlst[0],op[0],op[1],op[2],op[3])
    print(maxval)
    print(minval)