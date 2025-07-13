import sys
sys.setrecursionlimit(10**6)

def star(n):
    if n == 1:
        return ['*']
    else:
        prev = star(n-1)
        length = len(prev)
        res = []
        
        # up1
        res.append("*" * (length+4))
        # up2
        res.append("*" + " " * (length+2) + "*")
            
        # middle
        for row in prev:
            res.append("* " + row + " *")
        
        # bottom2
        res.append("*" + " " * (length+2) + "*")
        # bottom1
        res.append("*" * (length + 4))
        
        return res

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print('\n'.join(star(n)))