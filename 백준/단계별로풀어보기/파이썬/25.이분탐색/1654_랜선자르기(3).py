import sys

def lan(lst,k):
    left, right = 1, max(lst)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        count = sum(line//mid for line in lst)
        if count < k:
            right = mid - 1
        elif count == k:
            answer = mid
            left = mid + 1
        else:
            left = mid + 1
    return answer

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    print(lan(lst,k))