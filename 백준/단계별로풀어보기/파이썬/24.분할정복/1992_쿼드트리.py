import sys

result = []

def quadtree(n,lst):
    val = onezero(lst)
    if val is not None:
        result.append(val)
        return
    
    half = n // 2
    div1 = [row[:half] for row in lst[:half]]
    div2 = [row[half:] for row in lst[:half]]
    div3 = [row[:half] for row in lst[half:]]
    div4 = [row[half:] for row in lst[half:]]
    
    result.append('(')
    quadtree(half, div1)
    quadtree(half, div2)
    quadtree(half, div3)
    quadtree(half, div4)
    result.append(')')

def onezero(lst):
    start = lst[0][0]
    for row in lst:
        for element in row:
            if element != start:
                return None
    return start

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [list(sys.stdin.readline().strip()) for _ in range(n)]
    quadtree(n,lst)
    print(*result,sep='')