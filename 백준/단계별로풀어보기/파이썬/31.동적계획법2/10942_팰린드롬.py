import sys

if __name__ == "__main__":
    _ = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    query = int(sys.stdin.readline())
    
    res = []
    for _ in range(query):
        s, e = map(int, sys.stdin.readline().split())
        res.append()
        
    print('\n'.join(map(str, res)))