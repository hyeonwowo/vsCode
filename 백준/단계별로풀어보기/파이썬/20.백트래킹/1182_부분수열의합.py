import sys
sys.setrecursionlimit(10**6)

def backtracking(start):
    global cnt
    if total:
        if sum(total) == S:
            cnt += 1
            return
    else:
        for i in range(start, N):
            total.append(lst[i])
            backtracking(i+1)
            total.pop()
        
if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    
    total = []
    cnt = 0
    backtracking(0)
    print(cnt)