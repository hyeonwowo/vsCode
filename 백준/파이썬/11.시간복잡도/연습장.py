import sys

def changeDef(lst,c,n):
    i = len(lst) - 1
    gn = c * (n ** (len(lst) -1))
    fn = 0
    for element in lst:
        fn += (element * (n ** i))
        i -= 1
    return 1 if fn <= gn else 0

if __name__ == "__main__":
    lst = list(map(int, sys.stdin.readline().split()))
    c = int(input())
    n = int(input())
    print(changeDef(lst,c,n))

