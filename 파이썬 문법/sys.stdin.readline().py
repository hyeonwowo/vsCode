import sys

# ✅ 개요
# sys.stdin.readline()은 표준 입력에서 한 줄을 읽어오는 함수
# 많은 양의 입력을 빠르게 읽을 때 input()보다 훨씬 효율적
# 입력 문자열 끝에 \n 개행 문자가 포함되므로 보통 strip()과 함께 사용

# 기본 사용법
line = sys.stdin.readline()
line = line.strip() # \n 제거

# 정수 여러개 입력
x, y, z = map(int, input("").split()) # 기존 input 사용 (느림)
x, y, z = map(int, sys.stdin.readline().split())

# 여러 줄 입력받기
n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().strip()
    print(line)
    
    
# ✅ 특징 비교 (input() vs sys.stdin.readline())
# 항목	             input()	sys.stdin.readline()
# 속도	             느림	     빠름 (C로 구현)
# 개행 문자 포함 여부   포함 안 됨	  포함됨 (\n 있음)
# strip() 필요 여부	  필요 없음     필요함 (.strip())
# 사용 환경	          일반 코드	    알고리즘 대회, 대용량 입력