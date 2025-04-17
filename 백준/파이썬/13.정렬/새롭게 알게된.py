# 엔터(enter)로 연속 입력
lst = [int(input()) for _ in range(5)]


# sort()와 sorted()

# sort() : 리스트만 사용 가능, lst.sort()
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# sorted() : 모든 반복 가능한 객체, new_lst = sorted(lst)
numbers = [3, 1, 4, 2]
new_numbers = sorted(numbers)
print(numbers)      
print(new_numbers)


# 공통옵션
names = ["apple", "banana", "cherry"]

# 길이 기준 오름차순 정렬
sorted_names = sorted(names, key=len)
print(sorted_names)  # ['apple', 'banana', 'cherry']

# 길이 기준 내림차순 정렬
names.sort(key=len, reverse=True)
print(names)         # ['banana', 'cherry', 'apple']


# 파이썬에는 avg() 메서드가 없다 !

# lst.sort()와 함수 인자
def printlst(lst):
    print(lst)
    
lst = [5,3,4,2,1]
print(lst.sort()) # None 출력 : lst.sort() 는 lst를 수정하고, None을 반환
lst.sort
print(lst.sort()) # 정렬된 리스트 출력


# sys.stdout.write("") : 출력시 print()보다 더 빠른 속도 보장
import sys
element = 100
sys.stdout.write(f"{element}\n")

# counting 정렬
# 정렬시 리스트에 넣어서 정렬하는것보다, 들어오는 즉시 처리하는게 더 빠르다
# 리스트로 무언가를 다룬다는것은 편하긴 하지만 느림
# ex) i * count[i] : 느림

# ex) for i in range(count[i]) : 빠름
#         print(i)


# lst.reverse()
# 리스트 전용 메서드
# 리스트를 제자리에서 거꾸로 뒤집음
# 리턴값은 None

lst = [1,2,3]
lst.reverse()
print(lst)


# reversed(lst)
# 모든 반복 가능한 객체에서 사용 가능
# 원본을 변경하지 않고, 역순 반복자 리턴
# 출력 혹은 리스트 변환 후 사용

lst = [1,2,3]
revlst = reversed(lst)
print(list(revlst)) # [3,2,1]
print(lst) # [1,2,3] : 원본은 그대로