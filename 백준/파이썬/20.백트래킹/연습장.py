import sys

def findparent(a,b):
    
    return str()

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    result = []
    for _ in range(n):
        result.append(findparent(*map(int, sys.stdin.readline().split())))
    print('\n'.join(result))