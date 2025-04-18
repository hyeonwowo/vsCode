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


# 리스트는 순차탐색 O(n), set은 해시탐색 O(1) : 만약 둘다 사용 가능하다면 set을 사용하자

# 한번에 두개 인자 받기
def pocketmon():
    pass
print(pocketmon(*map(int, sys.stdin.readline().split())))


# 숫자 -> 이름 : 이름 -> 숫자
# 딕셔너리 두개 사용하는게 효율적 !
name_to_num = {}
num_to_name = {}