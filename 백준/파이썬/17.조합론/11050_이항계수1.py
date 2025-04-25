import sys

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def main(n,k):
    return factorial(n) // factorial(k) // factorial(n-k)

if __name__ == "__main__":
    print(main(*map(int, sys.stdin.readline().split())))