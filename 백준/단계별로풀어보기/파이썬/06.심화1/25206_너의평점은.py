import sys

def score(lst):
    
    dictScore = {
        'A+':4.5,
        'A0':4.0,
        'B+':3.5,
        'B0':3.0,
        'C+':2.5,
        'C0':2.0,
        'D+':1.5,
        'D0':1.0,
        'F':0.0,
    }
    
    grade_count = 0 # 학점의 총합
    total_score = 0 # 학점 * 과목평점
    for element in lst:
        object, str_point, grade = element
        point = float(str_point)
        if grade == 'P': 
            continue
        grade_count += point
        total_score += (point * dictScore[grade])
    return total_score / grade_count
if __name__ == "__main__":
    lst = []
    for _ in range(20): # 20으로 변경 !
        object, point, grade = list(sys.stdin.readline().split())
        lst.append((object,point,grade))
    print(score(lst))    
    