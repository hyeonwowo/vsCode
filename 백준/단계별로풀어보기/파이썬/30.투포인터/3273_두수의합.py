import sys

def twoPointer(lst, N):
    count = 0
    left = 0
    right = len(lst) - 1
    total = 0
    
    while left < right:
        total = lst[left] + lst[right]
        if total < N:
            left += 1
        elif total > N:
            right -= 1
        else:
            count += 1
            left += 1
            right -= 1
            
    return count

if __name__ == "__main__":
    _ = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    N = int(sys.stdin.readline())
    print(twoPointer(sorted(lst),N))