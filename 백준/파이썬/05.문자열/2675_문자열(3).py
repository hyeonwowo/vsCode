import sys

def strRepeat(N):
    for _ in range(N):
        resultLst = []
        repeat, st = list(sys.stdin.readline().split())
        for ch in st:
            resultLst.append(ch*int(repeat))
        result = "".join(resultLst)
        print(result)

if __name__ == "__main__":
    N = int(input())
    strRepeat(N)