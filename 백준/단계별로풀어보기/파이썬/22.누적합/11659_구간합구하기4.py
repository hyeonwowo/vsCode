import sys
input = sys.stdin.readline

def totalsum():
    prevsum = [0]  
    for i in range(len(numlst)):
        prevsum.append(prevsum[-1] + numlst[i])
    return prevsum

if __name__ == "__main__":
    N, M = map(int, input().split())
    numlst = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(M)]
    
    total = totalsum()
    result = []
    
    for a, b in data:
        result.append(total[b] - total[a - 1])
    
    print('\n'.join(map(str, result)))
