import sys

def numsequence():
    prev = [sum(numlst[:M])]
    maxnum = -float('inf')
    for i in range(N-M+1):
        prev.append(prev[i] + numlst[i+M] - numlst[i])
    del prev[0]
    return max(prev)
if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    numlst = list(map(int, sys.stdin.readline().split()))
    numlst.insert(0,0)
    print(numsequence())