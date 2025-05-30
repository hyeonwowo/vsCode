import sys

def strIndex(st,n):
    return st[n-1]
if __name__ == "__main__":
    st = sys.stdin.readline()
    n = int(sys.stdin.readline())
    print(strIndex(st,n))