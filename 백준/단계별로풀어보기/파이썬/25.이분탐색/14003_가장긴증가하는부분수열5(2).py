import sys

def binary_search(lst, target):
    start, end = 0, len(lst)
    while start < end:
        mid = (start + end) // 2
        if lst[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def lis(arr):
    n = len(arr)
    res = []     
    pos = [0] * n   

    for i in range(n):
        idx = binary_search(res, arr[i])
        if idx == len(res):
            res.append(arr[i])
        else:
            res[idx] = arr[i]
        pos[i] = idx

    return len(res), pos

def pathTo(arr, pos, lis_len):
    ans = [0] * lis_len
    cur = lis_len - 1
    for i in range(len(arr) - 1, -1, -1):
        if pos[i] == cur:
            ans[cur] = arr[i]
            cur -= 1
    return ans

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    lis_len, pos = lis(arr)
    subseq = pathTo(arr, pos, lis_len)

    print(lis_len)
    print(*subseq)
