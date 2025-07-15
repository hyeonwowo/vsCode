# ex1) 합이 M이 되는 연속된 부분 구간 개수 구하기
# 정수 배열 arr에서 합이 정확히 M이 되는 연속된 부분 구간의 개수를 구하라.

def twopointer(lst, M):
    n = len(lst)
    left = 0
    right = 0
    count = 0
    
    current_sum = 0
    while True:
        if current_sum >= M:
            current_sum -= lst[left]
            left += 1
        elif right == n:
            break
        else:
            current_sum += lst[right]
            right += 1
            
        if current_sum == M:
            count += 1
    
    return count

if __name__ == "__main__":
    lst = [1,2,3,2,5]
    M = 5
    print(twopointer(lst,M))
    