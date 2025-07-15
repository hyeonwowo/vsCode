import sys
sys.setrecursionlimit(10**6)

numcount = {-1:0, 0:0, 1:0}

def isColor(n, lst):
    color = lst[0][0]
    for i in range(n):
        for j in range(n):
            if lst[i][j] != color:
                return False
    return True

def paperCount(n, lst):
    if isColor(n, lst):
        color = lst[0][0]
        numcount[color] += 1
        return
    else:
        third = n // 3
        
        # 1 2 3
        lst1 = [row[:third] for row in lst[:third]]
        lst2 = [row[third:2*third] for row in lst[:third]]
        lst3 = [row[2*third:] for row in lst[:third]]
        
        # 4 5 6
        lst4 = [row[:third] for row in lst[third:2*third]]
        lst5 = [row[third:2*third] for row in lst[third:2*third]]
        lst6 = [row[2*third:] for row in lst[third:2*third]]
        
        # 7 8 9
        lst7 = [row[:third] for row in lst[2*third:]]
        lst8 = [row[third:2*third] for row in lst[2*third:]]
        lst9 = [row[2*third:] for row in lst[2*third:]]
    
        paperCount(third, lst1)
        paperCount(third, lst2)
        paperCount(third, lst3)
        
        paperCount(third, lst4)
        paperCount(third, lst5)
        paperCount(third, lst6)
        
        paperCount(third, lst7)
        paperCount(third, lst8)
        paperCount(third, lst9)
        

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    paperCount(n, lst)
    print(numcount[-1])
    print(numcount[0])
    print(numcount[1])
    