# 교점 구하는 공식
# 범위 (a <= x <= b, c <= y <= d)
# 교점이 있고, 범위 안에 존재하면 1
# 교점이 없거나(평행), 범위 밖에 존재하면 0

import sys

def findPoint(x1, y1, x2, y2, x3, y3, x4, y4):
    if ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)) == 0:
        return 0
    
    px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))//((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    py = ((x1*x2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))//((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    
    rangea = min(x1, x2, x3, x4)
    rangeb = max(x1, x2, x3, x4)
    rangec = min(y1, y2, y3, y4)
    ranged = max(y1, y2, y3, y4)
    
    if rangea <= px <= rangeb and rangec <= py <= ranged:
        return 1
    return 0
    
    
if __name__ == "__main__":
    L1 = list(map(int, sys.stdin.readline().split()))
    L2 = list(map(int, sys.stdin.readline().split()))
    
    query = L1 + L2
    print(findPoint(*query))