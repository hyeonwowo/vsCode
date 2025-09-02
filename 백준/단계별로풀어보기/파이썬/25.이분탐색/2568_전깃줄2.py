import sys

def binary_search(res, target):
    start, end = 0, len(res)
    while start < end:
        mid = (start + end) // 2
        if res[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def lis(n, line):
    res = []
    pos = [0] * n
    parent = [-1] * n  # 복원용

    lst = [b for _, b in line]
    for i in range(n):
        idx = binary_search(res, lst[i])
        if idx == len(res):
            res.append(lst[i])
        else:
            res[idx] = lst[i]
        pos[i] = idx

        # parent 연결
        if idx > 0:
            for j in range(i-1, -1, -1):
                if pos[j] == idx-1 and lst[j] < lst[i]:
                    parent[i] = j
                    break
    return len(res), pos, parent

def pathTo(length, pos, parent):
    # LIS 인덱스 복원
    curr = pos.index(length-1)
    seq_idx = []
    while curr != -1:
        seq_idx.append(curr)
        curr = parent[curr]
    seq_idx.reverse()
    return set(seq_idx)  # LIS에 포함된 인덱스 집합

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    line = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    line.sort()  # A 기준 정렬

    length, pos, parent = lis(n, line)
    lis_indices = pathTo(length, pos, parent)

    # 전체 인덱스 중 LIS에 없는 것 = 제거 대상
    remove = [line[i][0] for i in range(n) if i not in lis_indices]

    print(len(remove))
    for a in sorted(remove):
        print(a)
