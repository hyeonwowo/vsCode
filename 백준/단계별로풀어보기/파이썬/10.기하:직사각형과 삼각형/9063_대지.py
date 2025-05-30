import sys

def ground(n):
    xPoint = []
    yPoint = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        xPoint.append(x)
        yPoint.append(y)
    return (max(xPoint) - min(xPoint)) * (max(yPoint) - min(yPoint))

if __name__ == "__main__":
    print(ground(int(input())))