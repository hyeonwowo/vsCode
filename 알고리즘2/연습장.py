import random

point = [(5, 3), (6, 1), (1, 2), (2, 3), (1, 1), (4, 1), (3, 1)]

# y축 기준 정렬 후 x축 기준 정렬
sorted_point = sorted(point,key=lambda x:(x[1],x[0]))
print(sorted_point)