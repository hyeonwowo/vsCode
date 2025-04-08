# 새롭게 알게된
# 1. 한번에 여러 요소 입력받기 : x, y, z = map(int, sys.stdin.readline().split())
# 2. input보다 빠르게 데이터 입력받기 : sys.stdin.readline().split()
# 3. 배열 요소 한번에 바꾸기 : arr[x:y] = [new_element] * (y-x)
# 4. unpacking 연산자 : *arr (ex: [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3] [4,5,6] [7,8,9])


# 한번에 여러 요소 입력받기 - map()
x, y, z, = map(int, input("").split())
print(x, y, z)

# sys.stdin.readline().split() - input보다 빠르게 데이터 입력받기
import sys

line = sys.stdin.readline()
print(line)

x, y, z = sys.stdin.readline().split()
print(x, y, z)

# 배열 요소 한번에 바꾸기
arr = [None for _ in range(5)]
print(arr)
x, y = 1, 3
arr[x:y] = [99] * (y - x)
print(arr)

# * - unpacking 연산자
arr = [1,2,3]
print(arr) # [1,2,3]
print(*arr) # 1 2 3

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(*arr) # arr은 arr[0] arr[1] arr[2]로 다루기 편하게 만들어줌. 하지만, arr이 복사되거나 바뀌는것이 아님. 함수 호출 시 일시적인 언패킹전달 arr내부 구조에는 아무 영향이 없음
            # print(*arr)은 arr을 세 조각으로 나눠서 print함수에 넘기기만 할 뿐
new_arr = zip(*arr) # zip() : "튜플"의 형태로 여러 리스트를 함께 묶어줌 (리스트 길이가 다를 땐, 크기가 가장 작은 리스트 기준으로 튜플 개수 생성)
print(list(new_arr))