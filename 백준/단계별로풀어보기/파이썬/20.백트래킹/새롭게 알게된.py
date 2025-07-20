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
import sys

    # 정상 종료
sys.exit(0)  # 0은 성공적으로 종료되었음을 의미 (관례)

    # 비정상 종료
sys.exit(1)  # 1은 에러가 발생했음을 의미


# remove ? discard ? : remove 없는 요소 제거시, 오류발생. discard 없는 요소 제거시 그냥 넘어감.
lst = [1,2,3,4,5]
st = set([1,2,3,4,5])

lst.remove(6) # 오류발생 !
st.discard(6) # 오류 발생하지 않음


# 왠만하면 예약어와 같은 이름의 변수 사용을 하지 말자.
min = a[0] # 오류발생 !
min(1,2) # min()이 아닌 min = a[0] 변수로 받아들이게 됨


# set() 연산
st = set() # 선언
st.add(1) # 요소 추가
st.add(1)
st.add(2)

st.add(tuple([1,2,3])) # 리스트를 set에 넣을 땐 tuple()


# sorted() sort()
lst = [1,3,2,0]
lst.sort() # lst 자체를 정렬
newlst = sorted(lst) # 새로운 리스트 반환


# global 변수 : 함수 내부에서, 함수 밖에서 선언한 변수를 나눠쓰고 싶을 때 사용
# 예제1)
count = 0  # 전역 변수

def increase():
    global count  # 전역 변수임을 선언
    count += 1

increase()
increase()
print(count)  # 출력: 2


# 예제2)
count = 0

def increase():
    count += 1  # 에러 발생!
    # UnboundLocalError: local variable 'count' referenced before assignment

increase()


# 백트래킹에서 리턴은 언제 할까?
# 목표가 특정 조건을 만족하는 순간 탐색을 종료해야 할 때
# 예: “첫 해답만 찾고 끝내기”, “최단거리 경로 리턴”, “사전 순 정답 하나만 리턴”


# 모든 경우의 수 고려 - 백트래킹 사용