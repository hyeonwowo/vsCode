import sys

def finalSum(N):
    gradeList = list(map(int, sys.stdin.readline().split()))
    M = max(gradeList)
    NewList = [(i*100/M) for i in gradeList]
    return sum(NewList) / N    

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(finalSum(N))
