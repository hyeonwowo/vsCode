# 이진탐색 최대값, 최소값 찾기 : 배열이 주어졌을때, 한 요소보다 작거나 같은 요소 찾기

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    answer = -1
    while left <= right:  
        mid = (left + right) // 2
        if arr[mid] < target:
            answer = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return arr[mid]
    return arr[answer]

if __name__ == "__main__":
    lst = [1,3,5,7,9,11,13,15,17,19]
    print(binary_search(lst, 1)) # 1
    print(binary_search(lst, 9)) # 9
    print(binary_search(lst, 10)) # 9
    print(binary_search(lst, 19)) # 19
    print(binary_search(lst, 20)) # 19
    
    