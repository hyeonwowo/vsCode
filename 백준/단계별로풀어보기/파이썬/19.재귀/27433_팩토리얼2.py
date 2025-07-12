import sys
sys.setrecursionlimit(10**6)

def recur(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * recur(n-1)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(recur(n))