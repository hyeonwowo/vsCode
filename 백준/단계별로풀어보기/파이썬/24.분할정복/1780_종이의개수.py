import sys

result = {'-1':0,'0':0,'1':0}

def paper(n, lst):
    val = number(lst)
    if val is not None:
        result[str(val)] += 1
        return
        
    third = n // 3
    paper(third,[row[:third] for row in lst[:third]])
    paper(third,[row[third:third*2] for row in lst[:third]])
    paper(third,[row[third*2:] for row in lst[:third]])
    
    paper(third,[row[:third] for row in lst[third:third*2]])
    paper(third,[row[third:third*2] for row in lst[third:third*2]])
    paper(third,[row[third*2:] for row in lst[third:third*2]])
    
    paper(third,[row[:third] for row in lst[third*2:]])
    paper(third,[row[third:third*2] for row in lst[third*2:]])
    paper(third,[row[third*2:] for row in lst[third*2:]])
    
    
def number(lst):
    start = lst[0][0]
    for row in lst:
        for element in row:
            if element != start:
                return None
    return start

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    paper(n,lst)
    for element in result.values():
        print(element)