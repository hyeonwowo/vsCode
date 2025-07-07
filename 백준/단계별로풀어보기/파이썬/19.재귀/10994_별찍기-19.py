import sys
sys.setrecursionlimit(10**6)

def star(n):
    if n == 1:
        return "*"

if __name__ == "__main__":
    n = int(sys.stdin.readline().split())
    print(star(n))