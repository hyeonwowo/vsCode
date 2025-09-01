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
        if idx == len(res):
            res.append(lst[i])
        else:
            res[idx] = lst[i]
        pos[i] = idx      
    return len(res)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    print(n-lis(n, lst))