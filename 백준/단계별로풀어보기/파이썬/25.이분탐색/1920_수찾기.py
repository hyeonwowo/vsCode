import sys

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return 1
    return 0

def findnum(a, b):
    result = []
    for target in b:
        result.append(binary_search(a, target))
    return '\n'.join(map(str, result))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    lstt = list(map(int, sys.stdin.readline().split()))
        
    print(findnum(sorted(lst), lstt))