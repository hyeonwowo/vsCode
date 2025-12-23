import sys

def findTree(lst, cnt):
    mid = len(lst) // 2
    result[cnt].append(lst[mid])
    if len(lst) == 1:
        return
    else:
        cnt += 1
        findTree(lst[:mid], cnt)
        findTree(lst[mid+1:], cnt)
    
if __name__ == "__main__":
    L = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    cnt = 0
    result = [[] for _ in range(L)]
    findTree(lst, cnt)
    
    for i in range(L):
        print(*result[i])