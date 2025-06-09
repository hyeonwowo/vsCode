import sys

result = {"0":0,"1":0}

def paper(n,lst):
    value = color(lst)
    if len(lst) == 1:
        result[value] += 1
        return
    if color(lst):
        result[value] += 1
        return
    
    half = n // 2
    divide1 = [row[:half] for row in lst[:half]]
    divide2 = [row[half:] for row in lst[:half]]
    divide3 = [row[:half] for row in lst[half:]]
    divide4 = [row[half:] for row in lst[half:]]
    paper(half, divide1)
    paper(half, divide2)
    paper(half, divide3)
    paper(half, divide4)
    
def color(divide):
    length = len(divide)
    start = divide[0][0]
    for i in range(length):
        for j in range(length):
            if start != divide[i][j]: return False
    return str(start)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    paper(n,lst)
    print('\n'.join(list(map(str,result.values()))))