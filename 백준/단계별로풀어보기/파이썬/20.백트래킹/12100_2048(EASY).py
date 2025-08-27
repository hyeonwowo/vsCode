import sys
import copy
sys.setrecursionlimit(10**6)

def left(lst):
    newlst = [] # 0제거리스트
    for element in lst:
        if element != 0:
            newlst.append(element)

    res = []
    i = 0
    while i < len(newlst):
        if i+1 < len(newlst) and newlst[i] == newlst[i+1]:
            res.append(lst[i]+lst[i+1])
            i += 2
        else:
            res.append(lst[i])
            i += 1
    return res

def right(lst):
    newlst = [] # 0제거리스트
    for element in lst:
        if element != 0:
            newlst.append(element)

    newlst.reverse(0)
    res = []
    i = 0
    while i < len(newlst):
        if i+1 < len(newlst) and newlst[i] == newlst[i+1]:
            res.append(lst[i]+lst[i+1])
            i += 2
        else:
            res.append(lst[i])
            i += 1
    return res.reverse()

def up(lst):
    newlst = [] # 0제거리스트
    for element in lst:
        if element != 0:
            newlst.append(element)

    res = []
    i = 0
    while i < len(newlst):
        if i+1 < len(newlst) and newlst[i] == newlst[i+1]:
            res.append(lst[i]+lst[i+1])
            i += 2
        else:
            res.append(lst[i])
            i += 1
    return res

def down(lst):
    newlst = [] # 0제거리스트
    for element in lst:
        if element != 0:
            newlst.append(element)

    newlst.reverse(0)
    res = []
    i = 0
    while i < len(newlst):
        if i+1 < len(newlst) and newlst[i] == newlst[i+1]:
            res.append(lst[i]+lst[i+1])
            i += 2
        else:
            res.append(lst[i])
            i += 1
    return res.reverse()

def moveblock(dx, dy, board):
    if dx == -1 and dy == 0: # 좌측방향
        
        
        
    elif dx == 1 and dy == 0: # 우측방향



    elif dx == 0 and dy == -1: # 아래방향

    
    else: # 위방향


        

def backtracking(cnt, board):
    global maxval
    if cnt == 5:
        for row in board:
            for element in row:
                maxval = max(maxval, element)
        return
    else:
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            
        

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    maxval = 0
    
    backtracking(1, grid) 
    print(maxval)