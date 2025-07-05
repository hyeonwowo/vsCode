import sys

def draw_triangle(n):
    if n == 1:
        return ["  *  ", " * * ", "*****"]
    else:
        prev = draw_triangle(n - 1)
        height = len(prev)
        width = len(prev[-1])
        new = []

        # 위쪽 삼각형 (중앙 정렬)
        for line in prev:
            new.append(" " * (width // 2 + 1) + line + " " * (width // 2 + 1))

        # 아래쪽 삼각형 (두 개 나란히)
        for line in prev:
            new.append(line + " " + line)

        return new

def print_triangle(lst):
    return '\n'.join(lst)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    result = draw_triangle(n)
    print(print_triangle(result))
