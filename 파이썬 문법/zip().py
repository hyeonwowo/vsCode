# zip() : 여러개의 이터러블을 묶어서 같은 인덱스의 요소들을 튜플로 변환


# 기본 사용법
a = [1,2,3]
b = ["one","two","three"]

zipped = zip(a,b)
print(list(zipped))
print()


# 여러개의 리스트를 묶을 수도 있음
c = [11,22,33]
zipped = zip(a,b,c)
print(list(zipped))
print()



# zip()을 사용한 언패킹 : 튜를로 묶인 데이털르 다시 개별 리스트로 풀 수 있음.
x, y, z= zip(*[(1,11,111),(2,22,222),(3,33,333)])
print(x)
print(y)
print(z)