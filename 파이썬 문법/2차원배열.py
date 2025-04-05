# 2차원배열 기본형태
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# 2차원배열 생성 방법
# 1. 일반적인 수동 입력
arr = [[1,2,3],[4,5,6],[7,8,9]]

# 2. for 반복문을 활용한 생성
n,m = 3,4
arr = []

for _ in range(n):
    arr.append([0]*m)
    
    
# 3. 리스트 컴프리핸션
n, m = 3, 4
arr = [[0] * m for _ in range(n)]


# 2차원배열 입력 방법
# 1. 직접 입력한 숫자들을 2차원 배열로 받기
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(m)]
print(matrix)

# 행, 열 길이 구하기
arr = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

rows = len(arr)
cols = len(arr[0])

print(f"행의 개수: {rows}, 열의 개수: {cols}")
