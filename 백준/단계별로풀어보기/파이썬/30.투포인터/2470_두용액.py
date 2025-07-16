import sys

def twoWater(lst):
    left = 0
    right = len(lst) - 1
    
    minval = float('inf')
    cand1 = 0
    cand2 = 0
    
    while left < right:
        total = lst[left] + lst[right]
        if minval > abs(total):
            minval = abs(total) # total -> abs(total)
            cand1 = lst[left]
            cand2 = lst[right]
        
        # if, else 추가
        if total > 0:
            right -= 1
        else:
            left += 1
            
    return sorted([cand1, cand2])

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(*twoWater(sorted(lst)))