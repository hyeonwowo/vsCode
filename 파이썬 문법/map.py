# map은, 주어진 함수를 이터러블의 모든 요소에 적용한 결과를 반환.
# map(함수, 이터러블)
# 함수 : 각 요소에 적용할 함수 지정 (str(), int(), 사용자정의 함수 등 지정 가능)
# 이터러블 : 리스트, 튜플 등 반복 가능한 객체
 
numberList = [1,2,3,4,5]
print(numberList)

result = map(str,numberList) # numberList의 각 요소를 str형태로 변환
print(result) # OUTPUT : <map object at 0x1027e6be0>
print(list(result)) # OUTPUT : ['1', '3', '2', '5', '6']
print()


# map(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값으로, 새로운 리스트 반환
def power(n):
    return n*n

input_list = [1,2,3,4,5]
result_list = map(power,input_list)

print(result_list)
print(list(result_list))


# 한번에 여러 요소 입력
import sys
x, y, z, = map(int, sys.stdin.readline().split())
print(x, y, z)


# 리스트에 여러 요소 한번에 입력
gradeArr = list(map(int, sys.stdin.readline().split()))
print(gradeArr)
