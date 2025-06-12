import sys

def cuttree(m,height):
    left, right = 0, max(height)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        lengthsum = sum((length - mid) for length in height if length > mid) # 잘린 길이가 음수인 경우가 생김.. length - mid가 양수일 때만 반영
        if lengthsum < m:
            right = mid - 1
        elif lengthsum >= m:
            answer = mid
            left = mid + 1
    return answer

if __name__ == "__main__":
    _, m = map(int, sys.stdin.readline().split())
    height = list(map(int, sys.stdin.readline().split()))
    print(cuttree(m,height))