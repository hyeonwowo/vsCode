import sys
import math

N = int(sys.stdin.readline())
query = list(map(int, sys.stdin.readline().split()))

if query[0] == 1:
    k = query[1]
    nums = list(range(1, N + 1))
    k -= 1
    result = []

    for i in range(N):
        fact = math.factorial(N - i - 1)
        idx = k // fact
        result.append(nums[idx])
        nums.pop(idx)
        k %= fact

    print(*result)

else:
    perm = query[1:]
    nums = list(range(1, N + 1))
    rank = 1

    for i in range(N):
        idx = nums.index(perm[i])
        rank += idx * math.factorial(N - i - 1)
        nums.pop(idx)

    print(rank)
