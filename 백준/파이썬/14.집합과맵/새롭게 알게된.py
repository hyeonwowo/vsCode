# join은 문자열 리스트에만 적용
lst = [1,2,3,4,5]
print(' '.join(lst)) # 오류발생

lst = [1,2,3,4,5]
print(' '.join(map(str, lst))) # 문자열롭 변환해서 Join 사용 해야함

lst = ['a','b','c','d','e']
print(' '.join(lst)) # 정상작동