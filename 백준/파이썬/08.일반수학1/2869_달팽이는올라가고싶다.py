# 알고리즘은 맞지만 시간초과 발생
import sys

def snail(up,down,length):
    count = 1
    crnt_length = 0
    while True:
        crnt_length += up
        if crnt_length >= length:
            return count
        count += 1
        crnt_length -= down
        

if __name__ == "__main__":
    A,B,V = map(int, sys.stdin.readline().split())
    print(snail(A,B,V))