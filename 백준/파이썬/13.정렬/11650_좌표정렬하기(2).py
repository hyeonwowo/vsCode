import sys

def read_and_sort_points(n):
    points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    return sorted(points)

def print_points(points):
    print('\n'.join(f"{x} {y}" for x, y in points))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print_points(read_and_sort_points(n))
