# 2. 딕셔너리 활용
# 문제: 학생들의 점수를 딕셔너리로 입력받고, 평균 점수를 구하는 함수 average_score(scores)를 작성하세요.

def average_score():
    dictA = {}

    while 1:
        name = input("Type Name (None is over typing) >> ")
        
        if name == "none": 
            break

        score = int(input("Type Score >> "))

        if name not in dictA:
            dictA[name] = score
        else:
            sc = dictA[name]
            print("Update student score : ",sc,"->",score)
            dictA[name] = score

    sum = 0
    
    for i in dictA:
        sum += dictA[i]
    avg = sum // len(dictA)
    
    print(dictA)
    print(sum)
    print(round(avg,3)) # round(값, 소수점 자리수) : 특정 자리까지 반올림하여 출력
        
if __name__=="__main__":
    average_score()