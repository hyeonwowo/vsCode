# 한번에 여러 요소 입력받기 - map()
x, y, z, = map(int, input("").split())
print(x, y, z)

# sys.stdin.readline().split() - input보다 빠르게 데이터 입력받기
import sys

line = sys.stdin.readline()
print(line)

x, y, z = sys.stdin.readline().split()
print(x, y, z)
