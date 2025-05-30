import sys

def reverseInt(x, y):
    rX = x[::-1]
    rY = y[::-1]
    
    return rX if int(rX) > int(rY) else rY
    
if __name__ == "__main__":
    x, y = sys.stdin.readline().split()
    print(reverseInt(x,y))