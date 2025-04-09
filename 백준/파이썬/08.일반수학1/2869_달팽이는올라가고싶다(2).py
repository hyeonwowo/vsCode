import sys
import math

def snail_fast(up, down, height):
    length = up-down
    result = (height-down) // length # 전체 높이에서 미끄러지는 값을 빼, 그 전날까지의 누적 목표 생각
    return result

if __name__ == "__main__":
    A, B, V = map(int, sys.stdin.readline().split())
    print(snail_fast(A, B, V))
