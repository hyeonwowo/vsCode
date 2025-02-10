# 1. 리스트와 튜플 활용
# 문제: 사용자가 입력한 숫자 n개를 리스트로 저장한 후, 리스트의 모든 요소를 튜플로 변환하여 반환하는 함수 list_to_tuple()을 작성하세요

def list_to_tuple():
    listA = []
    while 1: # 일단 while은 무한루프로
        num = int(input("type num >> "))

        if num == -1: # 입력 받은 데이터를 기점으로 종료 수행
            return tuple(listA)
        
        listA.append(num) # 종료되지 않았더라면, 원하는 작업 수행

if __name__=="__main__":
    tupleA = list_to_tuple()
    print(type(tupleA),tupleA)
