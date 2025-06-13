import sys

def wifi(c, lst):
    start, end = 1, lst[-1] - lst[0]
    while start <= end:
        mid = (start + end) // 2
        current = lst[0]
        cnt = 1
        for i in range(1, n):
            if lst[i] >= current + mid:
                cnt += 1
                current = lst[i]
        if cnt >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

if __name__ == "__main__":
    n, c = map(int, sys.stdin.readline().split())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    print(wifi(c, sorted(lst)))