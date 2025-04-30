import sys

def backtrack(start):
    global cnt
    for i in N:
        if queen(start, i):
            
def queen(a,b):
    if 

if __name__ == "__main__":
    N = int(input())
    board = [0] * N
    cnt = 0
    backtrack(0)
    print(cnt)