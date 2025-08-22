import sys

def CCW(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

if __name__ == "__main__":
    x1, y1 = map(int, sys.stdin.readline().split())
    x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3 = map(int, sys.stdin.readline().split())
    
    res = CCW(x1, y1, x2, y2, x3, y3)
    if res < 0:
        print(-1)
    elif res == 0:
        print(0)
    else:
        print(1)