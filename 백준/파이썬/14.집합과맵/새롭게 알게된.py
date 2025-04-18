# join은 문자열 리스트에만 적용
lst = [1,2,3,4,5]
#print(' '.join(lst)) # 오류발생

lst = [1,2,3,4,5]
print(' '.join(map(str, lst))) # 문자열롭 변환해서 Join 사용 해야함

lst = ['a','b','c','d','e']
print(' '.join(lst)) # 정상작동


# 공백이 포함된 문자열이 들어왔을 때, 첫번째 문자열만 입력받기
import sys

log = sys.stdin.readline().split()[0] 
print(log) # adsf asdf -> asdf

logg = input().split()[0]
print(logg) # asdf asdf -> asdf


# 첫번째 "글자"만 입력받고 싶을때 

log = sys.stdin.readline()[0] 
print(log) # asdf asdf -> a

logg = input()[0]
print(logg) # asdf asdf -> a