import sys

result = {"0": 0, "1": 0}

def paper(n, lst):
    color_val = get_color(lst)
    if color_val is not None: # is not None(False) 구문을 통해 0이 반환돼더라도, 안전하게 처리
        result[str(color_val)] += 1
        return
    
    half = n // 2
    paper(half, [row[:half] for row in lst[:half]])   # 좌상
    paper(half, [row[half:] for row in lst[:half]])   # 우상
    paper(half, [row[:half] for row in lst[half:]])   # 좌하
    paper(half, [row[half:] for row in lst[half:]])   # 우하

def get_color(block):
    base = block[0][0]
    for row in block:
        for value in row:
            if value != base:
                return None # False도 가능
    return base # 0을 출력하는 경우에도, None처리를 통해 0을 숫자 그대로의 0으로 인식

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    paper(n, lst)
    print(result["0"])
    print(result["1"])
