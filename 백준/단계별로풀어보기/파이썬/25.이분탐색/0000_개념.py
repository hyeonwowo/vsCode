# 이분탐색 : 정렬된 배열에서 원하는 값을 효율적으로 찾는 알고리즘

# 전체조건 : 배열이 오름차순으로 정렬, 중간값을 기준으로 왼쪽 또는 오른쪽 절반으로 탐색 범위를 좁혀나감, 목표값이 중간값보다 작으면 왼쪽, 크면 오른쪽으로 범위를 좁힘

# 기본 이분 탐색 코드
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return None # 못찾은 경우