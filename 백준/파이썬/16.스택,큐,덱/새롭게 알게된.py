# 파이썬에서의 조건분기
#  False로 평가되는 것들:
# None
# False
# 숫자 0 (정수형 0, 실수형 0.0, 복소수 0j 등)
# 빈 시퀀스/컨테이너 ('', [], {}, set(), dict(), range(0) 등)

# 🟢 그 외의 모든 값은 True로 평가됩니다:
# 양의 정수 2, 3, 4, 음수 -1, -5 등: ✅ 참
# "hello", [1, 2], { "key": "value" }: ✅ 참

if 3:
    print("참입니다")  # 출력됨

if None:
    print("거짓입니다")  # 출력 안 됨

if []:
    print("빈 리스트입니다")  # 출력 안 됨

if [1]:
    print("요소가 있는 리스트입니다")  # 출력됨

print()

# 리스트 인덱싱 처리와 조건문 : 리스트가 비어있는 경우를 고려
lst = [1,2,3,4,5]

while True:
    if lst: # lst 자체만으로 비어 있는 경우를 알 수 있음
        print(lst.pop())
    else:
        print("None..")
        break
    
# Deque의 연산
# ✅ 주요 연산 정리
# 메서드	설명	시간복잡도
# append(x)	오른쪽 끝에 x 추가	O(1)
# appendleft(x)	왼쪽 끝에 x 추가	O(1)
# pop()	오른쪽 끝 요소 제거 후 반환	O(1)
# popleft()	왼쪽 끝 요소 제거 후 반환	O(1)
# extend(iter)	오른쪽 끝에 iterable 추가	O(k)
# extendleft(iter)	왼쪽 끝에 iterable 추가 (순서 반대로 들어감)	O(k)
# clear()	모든 요소 제거	O(n)
# reverse()	순서를 반대로 뒤집음	O(n)
# rotate(n=1)	회전: 오른쪽으로 n칸 이동 (음수면 왼쪽으로)	O(k)
from collections import deque

dq = deque()

# 삽입
dq.append(1)        # dq: [1]
dq.appendleft(2)    # dq: [2, 1]

# 삭제
dq.pop()            # → 1, dq: [2]
dq.popleft()        # → 2, dq: []

# 확장
dq.extend([3, 4])         # dq: [3, 4]
dq.extendleft([1, 2])     # dq: [2, 1, 3, 4]

# 회전
dq.rotate(1)        # dq: [4, 2, 1, 3]
dq.rotate(-2)       # dq: [1, 3, 4, 2]

# 기타
dq.clear()          # dq: []
