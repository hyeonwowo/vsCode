import sys
sys.setrecursionlimit(10**6)

def star(n):
    if n == 3:
        return ['  *  ',
                ' * * ',
                '*****']
    else:
        prev = star(n // 2) # 입력 : 3 * (2 ** n)
        res = []

        # 상단 (기존 삼각형 "중앙 정렬')
        for row in prev:
            res.append(' ' * (n // 2) + row + ' ' * (n // 2)) # n == 6 좌우 + 3, n == 12 좌우 + 6 ... (n // 2) 규칙 생성 

        # 하단 (기존 삼각형 두 개를 좌우에 붙임)
        for row in prev:
            res.append(row + ' ' + row) # 각 삼각형 줄마다 공백 (__*__, _*_*_, *****) 포함 -> row + ' ' + row에서 ' ' 이 하나밖에 없는 이유

        return res

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print('\n'.join(star(n)))
