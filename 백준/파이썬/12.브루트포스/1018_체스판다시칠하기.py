import sys

def startPoint(lst,n,m):
    spx, spy = n - 8 + 1, m - 8 + 1
    mincolor = float('int')
    for x in range(spx+1):
        for y in range(spy+1):
            colorcount = colorChess(lst[x][y],lst)
            if mincolor > colorcount:
                mincolor = colorcount
    return colorcount
                
def colorChess(color,lst):
    count = 0
    for row in range(1,9):
        for col in range(1,9):
            if (row + col) % 2 == 0 and lst[row][col] != color:
                count += 1
            elif (row + col) % 2 != 0 and lst[row][col] == color:
                count += 1
    return count
      
if __name__ == "__main__":
    n,m = map(int, sys.stdin.readline().split())
    lst = [[] for _ in range(n)]
    for i in range(n):
        lst[i] = (sys.stdin.readline().strip())
    print(startPoint(lst,n,m))
       