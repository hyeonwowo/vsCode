import sys

def solve_linear(a, b, c, d, e, f):
    denominator = a * e - b * d
    if denominator == 0:
        return None  # 해가 없거나 무한
    x = (c * e - b * f) // denominator
    y = (a * f - c * d) // denominator
    return x, y

if __name__ == "__main__":
    a,b,c,d,e,f = map(int, sys.stdin.readline().split())
    print(*solve_linear(a,b,c,d,e,f))