import sys

def sumarr(arr1, arr2, n, m):
    arr3 = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr3[i][j] = arr1[i][j] + arr2[i][j]
    return arr3

def makearr(m):
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    return arr

def printarr(arr): # 런타임에러 발생
    for row in arr:
        for element in row: 
            print(element, end=' ')
        print()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr1 = makearr(n)
    arr2 = makearr(n)
    arr3 = sumarr(arr1, arr2, n, m)
    printarr(arr3)