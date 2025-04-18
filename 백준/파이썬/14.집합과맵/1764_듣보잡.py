import sys

def nonlookhear(n,m):
    notlook = [sys.stdin.readline().strip() for _ in range(n)]
    nothear = [sys.stdin.readline().strip() for _ in range(m)]
    
    result = list(set(notlook) & set(nothear))
    
    print(len(result))
    return '\n'.join(sorted(result))

if __name__ == "__main__":
    print(nonlookhear(*map(int, sys.stdin.readline().split())))