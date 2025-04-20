import sys
import math

def findnum(n,m):
    lst = []
    for k in range(n,m+1):
        if k == 1: continue
        if num(k): lst.append(k)
    return '\n'.join(map(str,lst))

def num(k):
    for i in range(2, (math.isqrt(k) + 1)):
        if k % i == 0: return False
    return True

if __name__ == "__main__":
    print(findnum(*map(int, sys.stdin.readline().split())))