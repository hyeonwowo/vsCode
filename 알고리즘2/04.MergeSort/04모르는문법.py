# 해당 페이지에서 모르는 문법 정리

# 리스트에 요소 합쳐서 추가 lista.append((i,lista[i])) : 튜플 형태로 추가해야함
lista = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
result = []
for i in range(len(lista)):
    result.append((i,lista[i]))

print(result)