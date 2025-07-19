import sys

def findcandidate(lst,x,y):
    rowcand = set()
    colcand = set()
    sqcand = set()
    
    for i in range(9):
        rowcand.add(lst[i][y])
        colcand.add(lst[x][i])

    tx, ty = (x // 3) * 3, (y // 3) * 3
    
    for i in range(3):
        for j in range(3):
            sqcand.add(lst[tx+i][ty+j])
    
    used = rowcand | colcand | sqcand
    return sett

if __name__ == "__main__":
    n = 9
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    sett = set([1,2,3,4,5,6,7,8,9])
    print(findcandidate(lst, 0, 0))