# 한번에 여러 요소 입력받기 - map()
x, y, z, = map(int, input("").split())
print(x, y, z)

# sys.stdin.readline().split() - input보다 빠르게 데이터 입력받기
import sys

line = sys.stdin.readline()
print(line)

x, y, z = sys.stdin.readline().split()
print(x, y, z)

# 배열 요소 한번에 바꾸기
arr = [None for _ in range(5)]
print(arr)
x, y = 1, 3
arr[x:y] = [99] * (y - x)
print(arr)

# * - unpacking 연산자
arr = [1,2,3]
print(arr) # [1,2,3]
print(*arr) # 1 2 3