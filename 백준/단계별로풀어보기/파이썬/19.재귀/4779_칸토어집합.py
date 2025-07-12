import sys
sys.setrecursionlimit(10**6)

def cantoa(st):
    length = len(st)
    if length == 1:
        return st
    else:
        return cantoa(st[:length//3]) + " " * (length // 3) + cantoa(st[2*length//3:])

if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)
        st = '-' * (3 ** n)
        print(cantoa(st))