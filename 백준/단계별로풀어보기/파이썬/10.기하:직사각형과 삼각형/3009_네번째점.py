import sys

def findPoint():
    dictX = {}
    dictY = {}
    for _ in range(3):
        x, y = map(int, sys.stdin.readline().split())
        if x not in dictX:
            dictX[x] = 1
        elif x in dictX:
            dictX[x] += 1
        if y not in dictY:
            dictY[y] = 1
        elif y in dictY:
            dictY[y] += 1    
    return f"{min(dictX, key=dictX.get)} {min(dictY, key=dictY.get)}"
    
if __name__ == "__main__":
    print(findPoint())