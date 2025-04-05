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

def printarr(arr):
    for row in arr:
        for element in row:
            print(element, end=' ')
        print()

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr1 = makearr(m)
    arr2 = makearr(m)
    arr3 = sumarr(arr1, arr2, n, m)
    printarr(arr3)