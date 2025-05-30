import sys
import math

def main(n):
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    resultlst = []
    for element in lst:
        if element <= 1:
            resultlst.append(2)
        else:
            resultlst.append(numnum(element))
    return '\n'.join(map(str, resultlst))

def findnum(k):
    for i in range(2, math.isqrt(k) + 1):
        if k % i == 0:
            return False
    return True

def numnum(i):
    while True:
        if findnum(i):
            return i
        i += 1

if __name__ == "__main__":
    print(main(int(input())))
