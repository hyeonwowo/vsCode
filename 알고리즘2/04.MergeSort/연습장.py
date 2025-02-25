# 연속하는 요소가 3개 이상인 인덱스의 처음과 끝 출력
def find_consecutive_ranges(lst,min_length=3):
    if not lst:
        return []
    
    point = 0
    count = 1

    for i in range(len(lst)):
        

lista = [1,2,3,3,3,4,5,5,5,5,5,6,7,8]

