# * - Unpacking 연산자 : *는 iterable (반복 가능한 객체) 의 요소를 하나하나 풀어서 사용하도록 해주는 연산자입니다. 
#                      대표적으로 리스트, 튜플, 문자열, range



# 1.print(*iterable)
arr = [1,2,3]
print(arr)
print(*arr)

# 2.함수 인자 전달시 사용
def sum(a,b,c):
    return a+b+c

arr = [1,2,3]
print(sum(*arr))

# 3.여러 리스트를 하나로 합칠 때
a = [1,2]
b = [3,4]
c = [*a, *b]

print(a)
print(b)
print(c)

# 4.튜플 문자열 등에도 사용 가능
print(*"abcde") # a b c d e
print(*range(5)) # 0 1 2 3 4

# 5.함수 정의에서의 *args
def sum(*arr):
    return sum(arr)

print(sum(1,2,3))
print(sum(10,20,30))

# ✅ 주의사항
# *는 iterable 객체에만 사용 가능

# unpacking 시 개수 불일치하면 TypeError 발생
