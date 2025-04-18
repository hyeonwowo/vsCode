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


# <주요 문자열 판별 메서드>
# 메서드 | 설명 | 예시
# str.isdigit() | 문자열이 숫자로만 이루어졌는지 |
# str.isalpha() | 문자열이 알파벳으로만 이루어졌는지 |
# str.isalnum() | 문자열이 알파벳 또는 숫자로 이루어졌는지 | 
# str.islower() | 모든 문자가 소문자인지 | 
# str.isupper() | 모든 문자가 대문자인지 |
# str.isspace() | 모든 문자가 공백 문자인지 (' ', \t, \n) |

s1 = "123"
s2 = "abc"
s3 = "abc123"
s4 = "HELLO"
s5 = " "

print(s1.isdigit())   # True
print(s2.isalpha())   # True
print(s3.isalnum())   # True
print(s4.isupper())   # True
print(s5.isspace())   # True


# int, str 등 type 확인 : isinstance()
x = 123
y = "123"

print(isinstance(x,int))
print(isinstance(x,str))
print(isinstance(y,int))
print(isinstance(y,str))


# dict, lst, set등을 처리를 할 때 해당하는 element가 자료구조에 저장되지 않았을 때의 케이스를 고려하기


# 집합 연산
A={1,2,3,4}
B={3,4,5,6}

    # 합집합 (union)
print(A|B)
print(A.union(B))

    # 교집합 (intersection)
print(A&B)
print(A.intersection(B))

    # 차집합 (difference)
print(A-B)
print(A.difference(B))

    # 대칭 차칩잡 (symmetric difference) : 서로 다른 요소만 포함
print(A^B)
print(A.symmetric_difference(B))
