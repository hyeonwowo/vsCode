# 리스트 컴프리헨션은 리스트를 간결하게 생성하는 문법


data = [(10,0.5),(20,0.2),(30,0.8)]
result = [i for i,_ in data] # 튜플의 첫번째 요소만 추출
result2 = [i for _,i in data] # 튜플의 두번째 요소만 추출

print(result)
print(result2)