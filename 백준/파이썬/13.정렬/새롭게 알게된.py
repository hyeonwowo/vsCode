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
