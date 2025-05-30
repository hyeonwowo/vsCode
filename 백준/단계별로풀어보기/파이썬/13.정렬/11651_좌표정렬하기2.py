import sys

def sortpoint(n):
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    sortedpoints = sorted(points, key=lambda x:(x[1],x[0]))
    return print('\n'.join(f"{x} {y}" for x,y in sortedpoints))

if __name__ == "__main__":
    sortpoint(int(input()))