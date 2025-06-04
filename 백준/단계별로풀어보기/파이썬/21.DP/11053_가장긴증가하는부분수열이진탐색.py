import sys

def binarytree(target, lis):
    start, end = 0, len(lis) - 1
    while start < end:
        mid = (start + end) // 2
        if lis[mid] == target:
            return mid
        elif lis[mid-1] < target < lis[mid]:
            return mid
        elif target < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start

def increasenum(lst):
    lis = [lst[0]]
    for i in range(1,n):
        target = lst[i]
        if lis[-1] < target:
            lis.append(target)
        else: # lis[-1] >= target
            idx = binarytree(target, lis)
            lis[idx] = target
            
    return len(lis)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(increasenum(lst))