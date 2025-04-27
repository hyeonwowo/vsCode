import sys

def draw_star(n):
    if n == 1: return ['***','* *','***']
    else:
        prev = draw_star(n-1)
        new = []
        print(len(prev)) # 1 - 3 - 9 - 27 ..
        # top
        for line in prev:
            new.append(line * 3)
        # middle
        for line in prev:
            new.append(line + ' '*len(prev) + line)
        # bottom
        for line in prev:
            new.append(line * 3)
        
        return new
    
def main(lst):
    return '\n'.join(lst)

if __name__ == "__main__":
    print(main(draw_star(int(input()))))