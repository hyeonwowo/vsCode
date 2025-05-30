import sys

def totalsum():
    prev = [0]
    for i in range(len(numlst)): # 0~4
        prev.append(prev[i] + numlst[i])
    return prev

if __name__ == "__main__":
    N,M = map(int, sys.stdin.readline().split())
    numlst = list(map(int, sys.stdin.readline().split()))
    inputdata = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    
    result = []
    totalprev = totalsum()
    for element in inputdata:
        a,b = element
        result.append(totalprev[b] - totalprev[a-1])
    print('\n'.join(map(str, result)))