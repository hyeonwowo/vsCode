# 딕셔너리 요소 출력
dicta = {0:'a',
         1:'b',
         2:'c'}

    # 1. for문을 이용한 출력 
for val in dicta.values():
    print(val)
print()

    # 2. list를 이용한 출력
lst = list(dicta.values())
print(lst)
print('\n'.join(lst))
print()

    # 3. values들을 공백으로 구분해서 출력
print(*dicta.values())
print()


# 무언가 아닐때, None, False 사용
def what():
    if 1 < 2:
        return None
    
if what() is not None: # is not None이라는 연산 사용
    print(",.,.")
print()


# 리스트 요소를 공백없이 출력하기
lst = [1,2,3,4,5,6,7,8,9]
print(*lst)
print(*lst, sep='') # sep !


# sep : print() 함수에 여러 값을 전달할 때, 각 값 사이에 들어갈 문자열 지정
# 기본 사용법: print(value1, value2, ..., sep='구분자')

# 1. 기본 출력 (sep 생략 → 공백)
print(1, 2, 3)  # 출력: 1 2 3

# 2. 쉼표로 구분
print(1, 2, 3, sep=', ')  # 출력: 1, 2, 3

# 3. 공백 없이 붙이기
print(1, 2, 3, sep='')  # 출력: 123

# 4. 특수 문자로 구분
print("A", "B", "C", sep='-')  # 출력: A-B-C
print("X", "Y", "Z", sep='\n')  
# 출력:
# X
# Y
# Z

# 5. end와 함께 사용 (end는 출력 후 마지막에 붙는 문자열)
print(1, 2, 3, sep=':', end=' END\n')  # 출력: 1:2:3 END
