import sys

def twoPointer(N, S, lst):
    left = 0
    right = 0
    total = 0
    minlen = float('inf')

    while True:
        if total >= S:
            minlen = min(minlen, right - left)
            total -= lst[left]
            left += 1
        elif right == N:
            break
        else:
            total += lst[right]
            right += 1

    return 0 if minlen == float('inf') else minlen

if __name__ == "__main__":
    N, S = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    print(twoPointer(N, S, lst))
