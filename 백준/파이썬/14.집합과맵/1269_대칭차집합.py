import sys

def eocldckwlqgkq(n, m):
    setA = set(map(int, sys.stdin.readline().split()))
    setB = set(map(int, sys.stdin.readline().split()))
    return len(setA ^ setB)

if __name__ == "__main__":
    print(eocldckwlqgkq(*(map(int, sys.stdin.readline().split()))))