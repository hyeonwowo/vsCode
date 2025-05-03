import sys

def main():
    result = []
    for tup in typelst:
        a,b = tup
        if a == 0: a = 1
        result.append(sum(b)-sum(a-1))
    return '\n'.join(map(str,result))

def sum(k):
    sumresult = 0
    for k in range(k):
        sumresult += num[k]
    return sumresult

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    typelst = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    print(main())
