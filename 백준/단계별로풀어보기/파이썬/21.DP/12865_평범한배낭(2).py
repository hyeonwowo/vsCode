import sys

def oridnarybag(n,m,lst):
    pass

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(oridnarybag(n,m,lst))