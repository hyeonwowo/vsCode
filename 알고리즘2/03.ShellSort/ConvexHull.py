import timeit
import random
import math

def grahamScan(points):
    # 1. 시작점 선택 (y 오름차순, x 내림차순)
    start_point = min(points, key=lambda x: (x[1], -x[0]))

    # 2. 각도 계산 함수
    def calculate_angle(A, B):
        x1, y1 = A
        x2, y2 = B
        angle = math.atan2(y2 - y1, x2 - x1)
        angle_degree = math.degrees(angle)
        return (B, angle_degree if angle_degree >= 0 else angle_degree + 360)

    # 3. ccw 판단 함수 (반시계 방향이면 1, 시계 방향이면 -1, 직선이면 0)
    def ccw(i, j, k):
        area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
        return 1 if area2 > 0 else -1 if area2 < 0 else 0

    # 4. 시작점을 제외한 점들을 각도 기준으로 정렬
    angle_rank = [calculate_angle(start_point, point) for point in points if point != start_point] # 각도 구하기
    sorted_points = [start_point] + [p[0] for p in sorted(angle_rank, key=lambda x: x[1])] # 각도 기준 정렬, 각도 버리고 좌표만 + 시작좌표 포함

    # 5. 볼록 껍질 찾기 (스택 사용)
    hull = []
    for point in sorted_points:
        while len(hull) >= 2 and ccw(hull[-2], hull[-1], point) != 1:
            hull.pop()  # 볼록 껍질을 형성하지 않는 점을 제거
        hull.append(point)

    # 6. 🔥 마지막 검사: 마지막 점과 출발점을 검사하여 연결부 확인 🔥
    while len(hull) >= 3 and ccw(hull[-2], hull[-1], hull[0]) != 1:
        hull.pop()  # 연결부가 올바르지 않으면 마지막 점 제거

    return hull



def correctnessTest(intput, expected_output, correct):
    output = grahamScan(input)
    print(f"grahamScan({input})\n{output}")
    if output == expected_output: print("Pass")
    else:        
        print(f"Fail - expected output: {expected_output}")
        correct = False
    print()    

    return correct


def simulateNSquare(points):    
    points = sorted(points, key = lambda p: (p[1], -p[0])) 
    result = []
    for i in range(len(points)):
        points_with_angle = []
        for j in range(i+1, len(points)):
            x, y = points[j]
            points_with_angle.append((x, y, math.atan2(y - points[i][1], x - points[i][0])))
        points_with_angle = sorted(points_with_angle, key = lambda p: p[2])


'''
Unit Test
'''
if __name__ == "__main__":
    '''# ccw turns
    print(ccw((0,0), (-1,1), (-2, -1)))
    print(ccw((-1,1), (-2, -1), (0,0)))
    print(ccw((-2, -1), (0,0), (-1,1)))

    # non-ccw turns
    print(ccw((0,0), (-2, -1), (-1,1)))
    print(ccw((-2, -1), (-1,1), (0,0)))
    print(ccw((-1,1), (0,0), (-2, -1)))
    print(ccw((0,0), (-1, 1), (-2, 2))) # Straight line'''

    print("Correctness test for grahamScan()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    print()
    correct = True
    
    input = [(3, -1), (2, -2), (4, -1)]
    expected_output = [(2, -2), (4, -1), (3, -1)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(0, 0), (-2, -1), (-1, 1), (1, -1), (3, -1), (-3, -1)]
    expected_output = [(3, -1), (-1, 1), (-3, -1)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(4, 2), (3, -1), (2, -2), (1, 0), (0, 2), (0, -2), (-1, 1), (-2, -1), (-2, -3), (-3, 3), (-4, 0), (-4, -2), (-4, -4)]
    expected_output = [(-4, -4), (2, -2), (3, -1), (4, 2), (-3, 3), (-4, 0)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(2, 0), (2, 2), (1, -1), (0, 2), (-1, 1), (-2, -2)]
    expected_output = [(-2, -2), (1, -1), (2, 0), (2, 2), (0, 2), (-1, 1)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(2, 0), (2, 2), (1, -1), (0, 2), (-1, 1), (-2, -2), (-2, 2), (4, -4)]
    expected_output = [(4, -4), (2, 2), (-2, 2), (-2, -2)]
    correct = correctnessTest(input, expected_output, correct)

    # "342235" is a 6-digit number and is greater than the other 5-digit numbers
    input = [(342235, -23412), (-74545, 72345), (25812, -45689), (-45676, 24578), (45689, 0), (-74545, 0), (0, 45689), (0, -45689)]
    expected_output = [(25812, -45689), (342235, -23412), (-74545, 72345), (-74545, 0), (0, -45689)]
    correct = correctnessTest(input, expected_output, correct)
    
    print()
    print("Speed test for grahamScan()")
    if not correct: print("Fail (since the algorithm is not correct)")
    else:
        repeat = 10
        inputLength = 100
        minC, maxC = -1000000, 1000000
        points = [(random.randint(minC, maxC), random.randint(minC, maxC)) for _ in range(inputLength)]
        tCodeToCompare = timeit.timeit(lambda: simulateNSquare(points), number=repeat) / repeat
        tSubmittedCode = timeit.timeit(lambda: grahamScan(points), number=repeat) / repeat        
        print(f"Average running time of grahamScan() and simulateNSquare() with {inputLength} points: {tSubmittedCode:.10f} and {tCodeToCompare:.10f}")                
        if tSubmittedCode < tCodeToCompare * 0.1: print("Pass")
        else:
            print("Fail")
        print()