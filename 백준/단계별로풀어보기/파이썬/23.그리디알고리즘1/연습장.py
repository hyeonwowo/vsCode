import sys

def power(a,n):
    if n == 0:
        return 1
    
    half = power(a,n//2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * a

if __name__ == "__main__":
    a, n = map(int, sys.stdin.readline().split())
    print(power(a,n))