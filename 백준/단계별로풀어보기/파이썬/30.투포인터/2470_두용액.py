import sys

def twoPointer(lst):
    left = 0
    right = len(lst) - 1

    minval = float('inf')
    cand1 = 0
    cand2 = 0

    while left < right:
        total = lst[left] + lst[right]
        if abs(total) < minval:
            minval = abs(total)
            cand1 = lst[left]
            cand2 = lst[right]

        if total < 0: # total이 0보다 작을때, 현재 값보다 더 작게하면 (right -= 1) 0에서 멀어짐 -> left += 1을 통해 0에 더 가까워져보려는 시도를 하는것임
            left += 1
        else: # 위와 동일
            right -= 1
    
    return cand1, cand2

if __name__ == "__main__":
    _ = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    print(*sorted(twoPointer(lst)))
