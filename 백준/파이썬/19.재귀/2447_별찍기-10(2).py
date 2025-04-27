import sys

def draw_star(n):
    if n == 1:
        return ['***', '* *', '***']
    else:
        prev = draw_star(n-1)
        size = len(prev)
        new = []
        
        # 위쪽: prev + prev + prev
        for line in prev:
            new.append(line * 3)
        
        # 가운데: prev + 공백 + prev
        for line in prev:
            new.append(line + ' ' * size + line)
        
        # 아래쪽: prev + prev + prev
        for line in prev:
            new.append(line * 3)
        
        return new

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    k = 0
    while 3 ** k != n:
        k += 1

    result = draw_star(k)
    for line in result:
        print(line)
