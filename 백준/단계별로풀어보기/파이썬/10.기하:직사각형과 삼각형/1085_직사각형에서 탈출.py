import sys

def findlength(x,y,w,h):
    return min(x,y,w-x,h-y)

if __name__ == "__main__":
    x, y, w, h = map(int, sys.stdin.readline().split())
    print(findlength(x,y,w,h))