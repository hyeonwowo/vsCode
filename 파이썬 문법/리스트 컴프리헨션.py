# 리스트 컴프리헨션은 리스트를 간결하게 생성하는 문법
data = [(1,111),(2,222),(3,333)] # 원본 데이터
print(data)
print()

lista = [p[0] for p in data] # 튜플의 첫번째 요소만 추출
listaa = [p[1] for p in data] # 튜플의 두번째 요소만 추출

listb = [i for i,_ in data] # 튜플의 첫번째 요소만 추출
listc = [i for _,i in data] # 튜플의 두번째 요소만 추출

print(lista)
print(listaa)
print(listb)
print(listc)
