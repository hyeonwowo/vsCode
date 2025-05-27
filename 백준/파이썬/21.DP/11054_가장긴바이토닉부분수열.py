import sys

def upscale(lst):
    pass

def downscale(lst):
    pass

def bitonic(lst):
    up = upscale(lst)
    down = downscale(lst)
    
    upmax = up[-1]
    downmax = down[0]
    if upmax == downmax:
        up.pop()
        return up + down
    else:
        return up + down

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(bitonic(lst))