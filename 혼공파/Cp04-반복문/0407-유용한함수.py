# 리스트 적용 기본 함수.
    # min() - 리스트 최소값
    # max() - 리스트 최대값
    # sum() - 리스트 합산값

listA = [1,2,3,4,5]
print(min(listA))
print(max(listA))
print(sum(listA))
print()

    # 응용방법
print(min(1,2,3,4,5))
print(max(1,2,3,4,5))
    #print(sum(1,2,3,4,5)) : 이건 안됨.
print()


# reversed() 함수로 역 리스트 생성.

listA = [1,2,3,4,5]
listB = [10,11,12,13,14]
reversed_listA = reversed(listA)

print(listA)
print(list(reversed_listA))
print()


# reversed() 함수와 반복문

for i in reversed(listB):
    print(i)
print()