# 1. 리스트와 튜플 활용 문제
# 문제:
# 사용자로부터 여러 개의 숫자를 입력받아 리스트에 저장한 뒤, 다음과 같은 기능을 수행하는 함수를 작성하세요.

# 리스트에 있는 숫자의 합과 평균을 계산하는 함수 sum_and_avg(lst)
# 가장 큰 값과 가장 작은 값을 찾는 함수 find_max_min(lst)
# 리스트를 내림차순으로 정렬하는 함수 sort_desc(lst)

def sum_and_avg(lst): # 숫자 합 평균 (1) : 함수 만들어보기, (2) : 파이썬 제공 함수 사용
    total = 0
    for element in lst:
        total += element
    avg = total/len(lst)
    return total, avg


def find_max_min(lst): # 최대값, 최소값
    min = lst[0]
    max = lst[0]
    for element in lst:
        if element < min:
            min = element
        if element > max:
            max = element
    return min, max    
    
def sort_desc(lst): # 내림차순 정렬
    lst.sort(reverse=True)
    return lst

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8,9,10]
    listb = [10,9,8,7,6,5,4,3,2,1]
    listc = [11,55,22,77,88]

    print(lista, sum_and_avg(lista), find_max_min(lista), sort_desc(lista))
    print(listb, sum_and_avg(listb), find_max_min(listb), sort_desc(listb))
    print(listc, sum_and_avg(listc), find_max_min(listc), sort_desc(listc))

# 오답노트
# sum은 파이썬 내장 함수이므로 변수명으로 사용하지 않는 것을 권장 : sum -> total
# lst.sort(reversed=True) -> lst.sort(reverse=True)
# if __name__ == "main" -> if __name__ == "__main__"