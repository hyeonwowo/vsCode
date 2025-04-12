import sys

def changeTo(fn):
    f = str(fn)
    for i in range(0,len(fn),1):

def bigO(fn,c,n0):
    pass

if __name__ == "__main__":
    fn = map(int, sys.stdin.readline().split())
    c = int(input())
    n0 = int(input())
    print(bigO(fn,c,n0))
    