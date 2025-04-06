import sys

def makearr(m):
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    return arr

def sumarr(arr1, arr2, n, m):
    return [[arr1[i][j] + arr2[i][j] for j in range(m)] for i in range(n)]

def printarr(arr):
    for row in arr:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr1 = makearr(n)
    arr2 = makearr(n)
    arr3 = sumarr(arr1, arr2, n, m)
    printarr(arr3)