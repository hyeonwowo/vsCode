import sys

def startPoint(lst,n,m):
    spx, spy = n - 8, m - 8
    mincolor = float('inf')
    for x in range(spx+1):
        for y in range(spy+1):
            colorcount1 = colorChess(x,y,lst,"W")
            colorcount2 = colorChess(x,y,lst,"B")
            mincolor = min(mincolor, colorcount1, colorcount2)
    return mincolor
                
def colorChess(x, y, lst, start_color):
    count = 0
    for i in range(8):
        for j in range(8):
            expected = start_color if (i + j) % 2 == 0 else ('B' if start_color == 'W' else 'W')
            if lst[x + i][y + j] != expected:
                count += 1
    return count

if __name__ == "__main__":
    n,m = map(int, sys.stdin.readline().split())
    lst = [[] for _ in range(n)]
    for i in range(n):
        lst[i] = (sys.stdin.readline().strip())
    print(startPoint(lst,n,m))
       