def draw_star(n):
    if n == 1:
        return ["*"]

    prev = draw_star(n // 3) # 작은 블록을 먼저 만들고 그걸 조합해서 큰 정사각형을 만듦
    result = []

    for row in prev: # 맨 위 3줄 조립
        result.append(row * 3)  # 각 줄을 그대로 복제

    for row in prev: # 중간 3줄 조립 (가운데는 공백)
        result.append(row + " " * (n // 3) + row)  # 각 줄을 그대로 복제

    for row in prev: # 아래 3줄 조립
        result.append(row * 3)  # 각 줄을 그대로 복제

    return result


if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    print('\n'.join(draw_star(n)))


# <각 줄을 그대로 복제> 한다는 개념 이해
# Before
# ***
# * *  
# ***

# After (각 줄을 그대로 복제. ()안에 있는 것들은 각 줄을 그디로 복제한 요소)
# *** (***) (***) 
# * * (* *) (* *)
# *** (***) (***)
# 이런식으로 ?