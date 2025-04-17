import sys

def readsortpoint(n):
    lst = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
    return sorted(lst)

def printpoint(points):
    print('\n'.join(f"{point.x} {point.y}" for point in points))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    printpoint(readsortpoint(n))
