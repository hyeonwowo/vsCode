import math
import timeit
import random

def collinearPoints(points):
    result = set()  # 중복 방지
    for point in points:
        slopes = [] # 한 점 기준으로, 모든 다른 점들의 기울기를 저장할 리스트
        for other in points: # 기준점 제외 다른 점들 순회
            if other != point: # 자기 자신 제외
                if other[0] - point[0] == 0: # 동일한 x축 위에 있을 시 (새로선)
                    slope = float('inf')  # 수직선 기울기는 무한대 (새로 - 'inf', 가로 - 0)
                else:
                    slope = (other[1] - point[1]) / (other[0] - point[0]) # 기울기 구하는 공식 (y증가량 / x증가량)
                slopes.append((slope, other)) # 기울기와 점을 튜플 형태로 추가 [(기울기,(x,y)),(기울기,(x,y)),(기울기,(x,y)),(기울기,(x,y)),(기울기,(x,y))]
        
        # 기울기 기준 정렬 (x좌표 오름차순, y좌표 오름차순 추가)
        slopes.sort(key=lambda x: (x[0], x[1][0], x[1][1])) # 정렬 - (기울기, x좌표, y좌표) 순서

        count = 1
        start = 0
        min_count = 3  # 최소 3개 이상

        # 정렬한 기울기값을 토대로 연속하는 점 탐색. ex) [1,1,2,3,3,3,4,5,6,6,6,6,6] -> [3,5,8,12] 연속하는 기울기의 시작, 끝점 반환
        for i in range(1, len(slopes)):
            if slopes[i][0] == slopes[i - 1][0]: # 연속하는 요소가 같을 때
                count += 1 # 카운트 추가
            else: # 연속하는 요소가 다를 때
                if count >= min_count: # collinear_group : 같은 기울기를 가진 연속한 3개 이상의 점을, 기울기를 제외하고 점의 크기순으로 정렬 후 collinear_group에 저장 : 이때 [3,5,8,12]가 한번에 저장되는게 아닌, collinear_group 리스트에 3,5 저장 -> result에 추가[3,5], 8,12을 collinear_group에 저장 -> result에 추가[3,5,8,12]
                    collinear_group = sorted([point] + [slopes[j][1] for j in range(start, i)]) # "j" : 리스트 "컴프리핸션" 내에서 선언됨. 기울기 제외 좌표를 저장. +[point] : 시작점을 포함해서 정렬 후 collinear_group에 저장
                    result.add((collinear_group[0][0], collinear_group[0][1], collinear_group[-1][0], collinear_group[-1][1])) # 시작점x, 시작점y, 끝점x, 끝점y result에 저장
                start = i
                count = 1

        # 마지막 그룹 확인 : 모든 점들의 기울기가 같을 때. for 루프 안에 있는 else구문이 실행되지 않음 -> 오류 발생, 이에대한 처리로 해당 코드 삽입
        if count >= min_count:
            collinear_group = sorted([point] + [slopes[j][1] for j in range(start, len(slopes))])
            result.add((collinear_group[0][0], collinear_group[0][1], collinear_group[-1][0], collinear_group[-1][1]))
    
    # 점 p1,p2,p3,p4,p5가 있을 때, 한 반복에서 (p1 - p2,p3,p4,p5) 수행 후 result에 저장 -> (p2 - p1,p3,p4,p5) 연산 수행 후 result에 저장 --- -> (p5 - p1,p2,p3,p4) 수행후 함수 종료 후 result 반환

    return sorted(result)  # 정렬하여 결과 반환

def correctnessTest(input, expected_output, correct):
    output = collinearPoints(input)
    print(f"collinearPoints({input})\n{output}")
    if output == expected_output: print("Pass")
    else:        
        print(f"Fail - expected output: {expected_output}")
        correct = False
    print()    

    return correct


def simulateNSquareLogN(points):
    points = sorted(points, key=lambda p:(p[1], -p[0]))
    for i in range(0, len(points)):
        slopes = []
        for j in range(i+1, len(points)):
            if points[i][0] == points[j][0]: slopes.append((points[j][0], points[j][1], float('inf')))
            else: slopes.append((points[j][0], points[j][1], (points[j][1]-points[i][1])/(points[j][0]-points[i][0])))
        slopes.sort(key=lambda p:(p[1], p[2], p[0]))
        
        for j in range(1, len(slopes)):
            if slopes[j][2] == slopes[j-1][2]:
                for k in range(5): pass


'''
Unit Test
'''
if __name__ == "__main__":

    print("Correctness test for collinearPoints()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    print()
    correct = True

    # No collinear sets found, thus return the empty list []
    input = [(0,0),(1,1)]
    expected_output = []
    correct = correctnessTest(input, expected_output, correct)


    input = [(0,0), (1,1), (3,3), (4,4), (6,6), (7,7), (9,9)]
    expected_output = [(0,0,9,9)]    
    correct = correctnessTest(input, expected_output, correct)

    input = [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (8,0)]
    expected_output = [(1,0,8,0)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(7,0), (14,0), (22,0), (27,0), (31,0), (42,0)]
    expected_output = [(7,0,42,0)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,-2), (0,-53)]
    expected_output = [(0, -53, 0, 5)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(19000,10000), (18000,10000), (32000,10000), (21000,10000), (1234,5678), (14000,10000)]
    expected_output = [(14000,10000,32000,10000)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(12446,18993), (12798,19345), (12834,19381), (12870,19417), (12906,19453), (12942,19489)]
    expected_output = [(12446,18993,12942,19489)]
    correct = correctnessTest(input, expected_output, correct)


    input = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3)]
    expected_output = [(0,0,0,3), (1,0,1,3)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(10000,0), (0,10000), (3000,7000), (7000,3000), (20000,21000), (3000,4000), (14000,15000), (6000,7000)]
    expected_output = [(0, 10000, 10000, 0), (3000, 4000, 20000, 21000)]    
    correct = correctnessTest(input, expected_output, correct)    


    # Case where the same point appears multiple times
    input = [(1,1), (2,2), (3,3), (4,4), (2,0), (3,-1), (4,-2), (0,1), (-1,1), (-2,1), (-3,1), (2,1), (3,1), (4,1), (5,1)]
    expected_output = [(-3, 1, 5, 1), (1, 1, 4, -2), (1, 1, 4, 4)]
    correct = correctnessTest(input, expected_output, correct)    


    print()
    print("Speed test for collinearPoints()")
    if not correct: print("Fail (since the algorithm is not correct)")
    else:
        repeat = 10
        inputLength = 100
        minC, maxC = -1000000, 1000000
        points = [(random.randint(minC, maxC), random.randint(minC, maxC)) for _ in range(inputLength)]
        tCodeToCompare = timeit.timeit(lambda: simulateNSquareLogN(points), number=repeat) / repeat
        tSubmittedCode = timeit.timeit(lambda: collinearPoints(points), number=repeat) / repeat        
        print(f"Average running time of collinearPoints() and simulateNSquareLogN() with {inputLength} points: {tSubmittedCode:.10f} and {tCodeToCompare:.10f}")
        #print(f"{tSubmittedCode / tCodeToCompare}")
        if tSubmittedCode < tCodeToCompare * 3: print("Pass")
        else:
            print("Fail")
        print()
        
    