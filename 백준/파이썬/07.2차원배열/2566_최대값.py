import sys

def makeArr(m):
    return [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

def findMax(n,m,arr):
    maxValue = 0
    iPoint = jPoint = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > maxValue:
                maxValue = arr[i][j]
                iPoint, jPoint = i, j
    print(f"{maxValue}\n{iPoint+1} {jPoint+1}")

if __name__ == "__main__":
    n = m = 9 # 나중에 9로 변경하기
    arr = makeArr(m)
    findMax(n,m,arr)