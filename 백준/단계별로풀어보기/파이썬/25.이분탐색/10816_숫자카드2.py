import sys

input = sys.stdin.readline

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    n = int(input())
    alst = sorted(map(int, input().split()))
    m = int(input())
    blst = list(map(int, input().split()))

    # 직접 카운팅해서 저장 (dict 사용)
    count_dict = {}
    for target in blst:
        if target not in count_dict:
            count_dict[target] = upper_bound(alst, target) - lower_bound(alst, target)

    # 출력
    print(' '.join(str(count_dict[num]) for num in blst))
