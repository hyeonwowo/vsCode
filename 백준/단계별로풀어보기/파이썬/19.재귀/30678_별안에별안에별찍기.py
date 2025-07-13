import sys
sys.setrecursionlimit(10**6)

def star(n):
    if n == 0:
        return ['*']
    else:
        prev = star(n-1)
        res = []
        temp = len(prev)
        
        for row in prev:
            padding = ' ' * temp
            res.append(padding + padding + row + padding + padding)
        
        for row in prev:
            padding = ' ' * temp
            res.append(padding + padding + row + padding + padding)
    
        for row in prev:
            res.append(row + row + row + row + row) 
            
        for row in prev:
            padding = ' ' * temp
            res.append(padding + row + row + row + padding)
            
        for row in prev:
            padding = ' ' * temp
            res.append(padding + row + padding + row + padding)
            
        return res
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print('\n'.join(star(n)))