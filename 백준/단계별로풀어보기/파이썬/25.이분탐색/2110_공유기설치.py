import sys

def wifi(c, lst):
    pass

if __name__ == "__main__":
    n, c = map(int, sys.stdin.readline().split())
    lst = [int(sys.stdin.readline().split()) for _ in range(n)]
    print(wifi(c, sorted(lst)))