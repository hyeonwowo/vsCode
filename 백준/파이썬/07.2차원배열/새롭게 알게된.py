# join : 리스트(or 반복 가능한 요소들)에 있는 "문자열"들을 하나로 연결
# join() : 내부에 들어가는 인자는 반드시 str 형태
# 1. 예제
words = ['Hello', 'world', 'Python']
print(words)
result = ' '.join(words) # 여기서 join()의 인자는 반드시 str !
print(result)

print()

# 2. 숫자 리스트 연결
num = [1,2,3,4,5]
print(num)
result = ' '.join(map(str, num))
print(result)
result = '-'.join(map(str, num))
print(result)


# 2차원 배열 순회시 enumerate() 사용
import sys
n, m = 2, 2
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
print(arr)

for i, row in enumerate(arr):
    for j, element in enumerate(row):
        print(f"{(i,j)} {element}")
        
        
# 2차원 배열 생성시 : lst = [[] * n] 결과는 여전히 []
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

n = len(lst)      # 행의 개수
m = len(lst[0])   # 열의 개수

# 전치 배열 만들기: m개의 빈 리스트 생성
reverselst = [[0] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        reverselst[j][i] = lst[i][j]

print("원본:", lst)
print("전치:", reverselst)


# 한줄로 전치 배열 만들기
reverselst = [list(row) for row in zip(*lst)]
print(reverselst)

# 불규칙한 2차원 배열을 처리할 때 시퀀스
# 1) 열이 가장 긴 수치를 기준으로, 빈 공간을 ' '로 처리함
arr = [
    [1], # [' '][' '][' '][' '][' ']
    [2,3,4,5,6], # 열이 가장 긴 수치를 기준으로 나머지 열의 빈 부분을 채워줌
    [7,8] # [' '][' '][' '][' ']
]

# row : 가로줄
# col : 세로줄

def repairarr(arr,row):
    maxlen = max(len(line) for line in arr)
    for i in range(row):
        while len(arr[i]) < maxlen:
            arr[i].append(' ')
    return arr

# 2차원배열에서 행렬 구하기

print(len(arr)) # 행
print(len(arr[0])) # 열

# 2차원 배열을 세로방향으로 처리 시
def reversearr(arr):
    result = ""
    for j in range(len(arr[0])):       # 열 먼저
        for i in range(len(arr)):      # 행 다음
            result += arr[i][j]
    return result


# zip()을 사용한 세로읽기 처리(단, 모든 행의 길이가 동일해야함)
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def reversearr(arr):
    return ' '.join(char for col in zip(*arr) for char in col)

print(reversearr(arr))