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


# count() : 리스트 내에서 특정 값이 몇번 등장하는지 카운팅
lst = [1,0,2,0,3,5,0]
print(lst.count(0))
 