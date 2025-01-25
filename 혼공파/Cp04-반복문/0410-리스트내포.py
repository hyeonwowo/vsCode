# 리스트 내포

array = []

for i in range(0,20,2):
    array.append(i)

print(array)
print()

array = [i for i in range(0,20,2)]
print(array)
print()


# 조건문을 활용한 리스트 내포

array = [i for i in range(0,20,2) if i%2 == 0]
print(array)
print()