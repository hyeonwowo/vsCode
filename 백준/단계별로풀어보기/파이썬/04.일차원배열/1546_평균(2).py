import sys

def finalSum(N):
    gradeArr = list(map(int, sys.stdin.readline().split()))
    M = max(gradeArr)
    gradeArr = [(score / M) * 100 for score in gradeArr]
    avg = sum(gradeArr) / N
    return avg

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(finalSum(N))
