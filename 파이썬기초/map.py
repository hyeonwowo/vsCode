# map은, 주어진 함수를 이터러블의 모든 요소에 적용한 결과를 반환.
# map(함수, 이터러블)
# 함수 : 각 요소에 적용할 함수 지정 (str(), int(), 사용자정의 함수 등 지정 가능)
# 이터러블 : 리스트, 튜플 등 반복 가능한 객체
 
numberList = [1,2,3,4,5]
print(numberList)

result = map(str,numberList)
print(list(result))

