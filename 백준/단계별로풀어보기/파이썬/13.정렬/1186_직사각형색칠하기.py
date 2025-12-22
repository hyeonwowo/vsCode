import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())
rects = []
xs, ys = set(), set()

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    rects.append((x1, y1, x2, y2, i + 1))  # 번호는 1부터
    xs.add(x1)
    xs.add(x2)
    ys.add(y1)
    ys.add(y2)

# 1️. 좌표 압축
xs = sorted(xs)
ys = sorted(ys)

x_id = {x: i for i, x in enumerate(xs)}
y_id = {y: i for i, y in enumerate(ys)}

W = len(xs)
H = len(ys)

# 2️. 각 셀의 owner 계산
cells = []  # (owner, area)

for i in range(W - 1):
    for j in range(H - 1):
        xL, xR = xs[i], xs[i + 1]
        yB, yT = ys[j], ys[j + 1]
        area = (xR - xL) * (yT - yB)
        if area == 0:
            continue

        top = 0  # 가장 위에 보이는 직사각형 번호
        for x1, y1, x2, y2, idx in rects:
            if x1 <= xL and xR <= x2 and y1 <= yB and yT <= y2:
                top = max(top, idx)

        if top > 0:
            cells.append((top, area))

# 3. K개 조합 탐색
best_area = -1
best_choice = None

for comb in combinations(range(1, N + 1), K):
    S = set(comb)
    total = 0

    for owner, area in cells:
        if owner in S:
            # owner보다 큰 번호 중 선택된 게 있으면 가려짐
            blocked = False
            for x in S:
                if x > owner:
                    blocked = True
                    break
            if not blocked:
                total += area

    if total > best_area:
        best_area = total
        best_choice = comb
    elif total == best_area:
        if comb < best_choice:
            best_choice = comb

# 4. 출력
print(" ".join(map(str, best_choice)))
