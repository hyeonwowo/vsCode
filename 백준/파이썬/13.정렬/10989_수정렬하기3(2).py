import sys

def sortnum(lst):
    count = [0] * 10001
    for i in range(len(lst)):
        idx = lst[i]
        count[idx] += 1
    for i in range(len(count)):
        if count[i] > 0: 
            output((f"{i}\n") * count[i])
        
if __name__ == "__main__":
    input = sys.stdin.readline
    output = sys.stdout.write
    
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    sortnum(lst)