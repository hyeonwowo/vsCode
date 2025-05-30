import sys

def sortlst(n):
    return ''.join(sorted(str(n),reverse=True))

if __name__ == "__main__":
    n = sys.stdin.readline().strip()
    print(sortlst(n))