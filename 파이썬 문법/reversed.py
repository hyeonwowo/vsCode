# reversed(sequence) : sequence - str, list, tuple ...

# reversed(1) : 문자열 뒤집기

text = "hello"
result = reversed(text)
print("".join(result)) 

print()

# reversed(2) : 리스트 뒤집기

listA = [1,2,3,4,5]
result = reversed(listA)
print(list(result))

print()

# reversed(3) : 튜플 뒤집기

data = (10,20,30)
result = reversed(data)
print(tuple(result))

print()


# reversed(4) : 반복문에서 사용

number = [1,2,3,4,5]

for num in number:
    print(num, end=" ")
print()

for num in reversed(number):
    print(num)



# 주의 사항:
# 반환값이 이터레이터:

# reversed()는 결과를 즉시 리스트나 문자열로 반환하지 않고 이터레이터로 반환합니다.
# 따라서 list(), tuple(), "".join() 등을 사용해 명시적으로 변환해야 결과를 확인할 수 있습니다.
# 원본 데이터는 변경되지 않음:

# reversed()는 원본 데이터의 순서를 변경하지 않습니다. 대신 새로운 이터레이터를 생성합니다.
# 인덱스 접근 불가:

# 반환된 이터레이터는 인덱스를 통해 접근할 수 없습니다. 필요할 경우 리스트나 튜플로 변환해야 합니다.
