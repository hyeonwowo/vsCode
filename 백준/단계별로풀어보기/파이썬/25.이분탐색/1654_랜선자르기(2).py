import sys

def binary_search(lst, k):
    left, right = 1, max(lst) # [802, 743, 457, 539]
    answer = 0
    while left <= right:
        mid = (left + right) // 2 # mid = 401 : 랜선길이 401부터 시작 - 5개 제작 가능 -> 랜선길이를 더 줄여야함(더 많이 만들기 위해)
        count = sum(x // mid  for x in lst) # 현재 랜선길이로 만들수있는 랜선의 수 구하기
        if count >= k: # 랜선이 많거나 같을때
            answer = mid # 최대값을 구하기 위한 과정
            left = mid + 1 # 현재 랜선 길이 + 1 ~ 802까지 
        else: # 랜선이 부족할 때
            right = mid - 1 # 1 ~ 현재 랜선 길이 + 1
    return answer

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    print(binary_search(lst ,k))