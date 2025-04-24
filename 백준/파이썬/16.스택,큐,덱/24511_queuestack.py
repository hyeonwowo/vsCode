import sys

def insertdata():
    N = int(input())
    DS = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    M = int(input())
    C = list(map(int, sys.stdin.readline().split()))
    return N,DS,B,M,C

def main(N,DS,B,M,C):
    pass

if __name__ == "__main__":
    print(main(insertdata()))