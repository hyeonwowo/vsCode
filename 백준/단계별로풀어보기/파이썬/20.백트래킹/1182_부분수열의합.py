import sys

def backtracking():
    global cnt
    if total == S:
        cnt +=1 
        return
    else:
        
if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    
    cnt = 0
    backtracking()