import sys

def numSum(M,N):
    sum = 0
    for char in M:
        sum += int(char)
    return sum
        

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = sys.stdin.readline().strip()
    print(numSum(M,N))