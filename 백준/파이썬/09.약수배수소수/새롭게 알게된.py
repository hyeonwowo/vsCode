# 소수탐색 연산범위 설정
element = int(input()) 
for i in range(2, element): # 2부터 시작하기
    print(i)
    
# 나머지연산 : 큰거 % 작은거 (원하는 나머지 연산결과 도출)
print(4%1) # 0
print(4%2) # 0
print(4%3) # 1
print(4%4) # 0

# 만약 작은거 % 큰거 수행하면? : 작은수(4)가 그대로 출력됨
print(4%5) # 4
print(4%6) # 4
print(4%7) # 4
print(4%8) # 4
print(4%9) # 4


# 여러줄로 입력받고 싶을 때
import sys
a, b = map(int, sys.stdin.readline().split()) # 한줄로 입력 ex) 10 20

a = int(sys.stdin.readline()) # 여러줄로 입력 ex) 10
b = int(sys.stdin.readline()) # 여러줄로 입력 ex) 20 

