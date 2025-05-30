import sys

def main():
    input = sys.stdin.readline
    output = sys.stdout.write
    
    n = int(input())
    count = [0] * 10001
    
    for _ in range(n):
        ipt = int(input())
        count[ipt] += 1
    
    for i in range(1,10001):
        for _ in range(count[i]):
            output(f"{i}\n")

if __name__ == "__main__":
    main()