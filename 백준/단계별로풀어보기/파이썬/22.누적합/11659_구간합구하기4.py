import sys

def totalsum(lst, startend):
    length = len(lst)
    prev_totalsum = [0] * length
    prev_totalsum[0] = lst[0]
    for i in range(1, length):
        prev_totalsum[i] = prev_totalsum[i-1] + lst[i]
    prev_totalsum.insert(0,0)
        
    result = []
    for i in range(m):
        start, end = startend[i]
        indexsum = prev_totalsum[end] - prev_totalsum[start-1]
        print(indexsum)
    return '\n'.join(result)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    startend = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(totalsum(lst, startend))
        