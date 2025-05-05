# 2차원 배열 입력하기

import sys
sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)] # [[map(int, sys.stdin.readline().split())] for _ in range(n)] 으로 하는게 아닌, list(map ..) 형태로 해줘야함
# 입력
# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0
print(sudoku)


# 입력한 2차원 배열 출력
for row in sudoku:
    print(*row)

# count() : 리스트 내에서 특정 값이 몇번 등장하는지 카운팅
lst = [1,0,2,0,3,5,0]
print(lst.count(0))


# [i-1] + [i]의 인덱싱 처리 : [0] 인덱스를 추가해 인덱스 초과 오류를 방지한다
numlst    = [10, 20, 30, 40, 50]
prevsum   = [0, 10, 30, 60, 100, 150]  # 인덱스 1부터 의미 있음

# ex) 구간 [2, 4]의 합 = prevsum[4] - prevsum[1] = 100 - 10 = 90


# sys.exit() : 실행중인 파이썬 프로그램을 종료시킴. 0 - 정상종료, 1(0이 아닌 모든값) - 비정상종료. "message" - 메시지를 출력하고 비정상 종료
