# 시간복잡도 개선 (total 값을 넘겨줌)
import sys
sys.setrecursionlimit(10**6)

def backtracking(start, currentSum):
    global cnt
    if start > 0 and currentSum == S:
        cnt += 1
    
    for i in range(start, N):
        backtracking(i+1, currentSum + lst[i]) # 돌아올 때, currentSum + lst[i]에서 currentSum 값만 남으므로 pop과정이 따로 없어도 됨

if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    
    total = []
    cnt = 0
    backtracking(0,0)
    print(cnt)