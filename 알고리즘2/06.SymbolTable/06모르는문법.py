# 해당 페이지에서 모르는 문법 정리

import matplotlib.pyplot as plt

# 선분 좌표
x_values = [0, 15]
y_values = [1, 1]

# 선분 그리기
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label="Segment")
plt.xlim(-1, 16)  # x 축 범위 설정
plt.ylim(0, 2)    # y 축 범위 설정
plt.axhline(y=0, color='gray', linestyle='--')  # x축 표시
plt.axvline(x=0, color='gray', linestyle='--')  # y축 표시

plt.grid()
plt.legend()
plt.title("Line Segment from (0,1) to (15,1)")
plt.show()
