import sys

def binary_search(res, target):
    start = 0
    end = len(res)
    while start < end:
        mid = (start + end) // 2
        if res[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def lis(n, lst):
    res = []
    pos = [0] * n
    
    for i in range(n):
        idx = binary_search(res, lst[i])
        if idx == n:
            res.append(lst[i])
        else:
            res[idx] = lst[i]
        pos[i] = idx
        
    return len(res), position

def pathTo(lst, pos, length):
    pass

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    length, position = lis(n, lst)
    path = pathTo(lst, length, position)
    
    print(length)
    print(*path)
    
    print(position)