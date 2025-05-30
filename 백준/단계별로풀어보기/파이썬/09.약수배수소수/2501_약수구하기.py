import sys

def findmember(n,k):
    memberlst = []
    for i in range(1,n+1):
        if n%i == 0: memberlst.append(i)
    return 0 if len(memberlst) < k else memberlst[k-1]

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    print(findmember(n,k))