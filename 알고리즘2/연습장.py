import random
import math

def calculate_angle(A,B): # 시작점과, 나머지점들의 각도를 구해서, 점과 각도를 함께 반환
    x1,y1 = A # start_point
    x2,y2 = B # points

    angle = math.atan2(y2-y1, x2-x1)
    angle_degree = math.degrees(angle)

    if angle_degree < 0:
        angle_degree += 360

    return (B,angle_degree)
    
points = [(5, 3), (6, 1), (1, 2), (2, 3), (1, 1), (4, 1), (3, 1), (0, 0),(0,1),(1,0),(2,0)]

# y축 기준 정렬 후 x축 기준 정렬
sorted_point = sorted(points, key=lambda x: (x[1], -x[0]))
print(sorted_point)

start_point = sorted_point.pop(0)
print(sorted_point)
print(start_point)
print()
print()

angle_rank = []

for point in sorted_point:
    angle_rank.append(calculate_angle(start_point,point)) # 좌표와, 순서가 튜플 형태로 저장 -> 순서 기준으로 정렬

print(calculate_angle(start_point,start_point))
for point, angle in angle_rank:
    print(point,":",angle)
print()
# 각도순으로 정렬
angle = sorted(angle_rank,key=lambda x:x[1])
print(angle)

sorted_list = list(map(lambda x:x[0],angle))
sorted_points = list(map(lambda x: x[0], sorted(angle, key=lambda x: x[1], reverse=True)))
print(sorted_points)