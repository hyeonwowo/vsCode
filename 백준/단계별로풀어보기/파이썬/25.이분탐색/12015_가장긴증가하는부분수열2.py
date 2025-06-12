import sys

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = len(arr)  # 삽입 위치로 끝을 기본값
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

def LIS(lst):
    lis = [lst[0]]
    for i in range(1, len(lst)):
        target = lst[i]
        if lis[-1] < target:
            lis.append(target)
        else:
            idx = binary_search(lis, target)
            lis[idx] = target  # idx < len(lis)이 항상 보장됨
    return lis

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(len(LIS(lst)))
