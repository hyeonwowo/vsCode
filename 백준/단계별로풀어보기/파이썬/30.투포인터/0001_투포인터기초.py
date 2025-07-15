import sys # 정렬된 배열에서 두 수의 합이 target이 되는 쌍이 있는지 확인

def twopointer(lst, target):
    left = 0
    right = len(lst) - 1
    count = 0
    
    while left < right:
        total = lst[left] + lst[right]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            count += 1
            right -= 1
            left += 1
            
    return count

if __name__ == "__main__":
    lst = [1,3,5,7,9,11]
    target = 10
    print(twopointer(lst, target))
    
    