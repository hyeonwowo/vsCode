import sys

def bino_coef(n,k):
    if k == 0 or k == n: return 1
    return bino_coef(n-1,k) + bino_coef(n-1,k-1)

if __name__ == "__main__":
    print(bino_coef(*map(int, input().split())))