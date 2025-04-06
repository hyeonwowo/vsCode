import sys

def makearr(n):
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    return arr

def sumarr(arr1, arr2, n, m):
    return [[arr1[i][j] + arr2[i][j] for i in range(m)] for j in range(n)]

def printarr(arr):
    for row in arr:
        print(' '.join(map(str, row)))
    

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr1 = makearr(n)
    arr2 = makearr(n)
    arr3 = sumarr(arr1, arr2, n, m)
    printarr(arr3)