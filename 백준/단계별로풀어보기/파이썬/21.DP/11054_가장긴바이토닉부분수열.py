import sys

def bitonic(lst):
    # 1. 증가 부분 수열 (왼쪽에서 오른쪽)
    inc = [1] * n
    for i in range(n):
        for j in range(i):
            if lst[j] < lst[i]:
                inc[i] = max(inc[i], inc[j] + 1)
    
    # 2. 감소 부분 수열 (오른쪽에서 왼쪽)
    dec = [1] * n
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if lst[j] < lst[i]:
                dec[i] = max(dec[i], dec[j] + 1)
    
    # 3. 바이토닉 수열 최대 길이
    max_bitonic = 0
    for i in range(n):
        max_bitonic = max(max_bitonic, inc[i] + dec[i] - 1)

    return max_bitonic

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(bitonic(lst))
