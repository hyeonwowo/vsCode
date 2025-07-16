import sys

def sumnum(num, lst):
    left = 0
    right = len(lst) - 1
    count = 0
    
    while left < right:
        total = lst[left] + lst[right]
        if total < num:
            left += 1
        elif total == num:
            count += 1
            left += 1
            right -= 1
        else:
            right -= 1
    
    return count
        
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    num = int(sys.stdin.readline())
    print(sumnum(num, sorted(lst)))