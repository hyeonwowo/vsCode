from collections import deque

# 1️⃣ deque 생성
dq = deque([1, 2, 3, 4, 5])
print("초기 deque:", dq)

# 2️⃣ 요소 추가
dq.append(6)  # 오른쪽(뒤)에 추가
print("append(6):", dq)

dq.appendleft(0)  # 왼쪽(앞)에 추가
print("appendleft(0):", dq)

# 3️⃣ 요소 제거
dq.pop()  # 오른쪽(뒤)에서 제거
print("pop():", dq)

dq.popleft()  # 왼쪽(앞)에서 제거
print("popleft():", dq)

# 4️⃣ 여러 요소 추가
dq.extend([7, 8, 9])  # 오른쪽(뒤)에 여러 요소 추가
print("extend([7, 8, 9]):", dq)

dq.extendleft([-1, -2, -3])  # 왼쪽(앞)에 여러 요소 추가 (순서 반대)
print("extendleft([-1, -2, -3]):", dq)

# 5️⃣ 요소 회전
dq.rotate(2)  # 오른쪽으로 2칸 회전
print("rotate(2):", dq)

dq.rotate(-2)  # 왼쪽으로 2칸 회전 (원래대로 복구)
print("rotate(-2):", dq)

# 6️⃣ deque 반전
dq.reverse()
print("reverse():", dq)

# 7️⃣ deque 비우기
dq.clear()
print("clear():", dq)
