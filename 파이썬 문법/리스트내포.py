# 리스트내포

arrayA = [i for i in range(0,20,2)]
arrayB = [i*i for i in range(0,20,2)]

# 조건문 활용 리스트내포
arrayC = [i for i in range(0,20) if i%2 == 0]
arrayD = [i
           for i in range(0,20)
            if i%2 == 0] # 이런 형식으로 가독성 좋게 쓸 수 있음.


print(arrayA)
print(arrayB)
print(arrayC)
print(arrayD)