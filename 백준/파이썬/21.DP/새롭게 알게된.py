# 빈 리스트 생성시 None, 0 등으로 요소를 넣고 반복
lst = [] * 10 # 빈칸을 반복하므로 결국엔 []
print(lst)
print(len(lst))
print()

lst = [None] * 10
print(lst)
print(len(lst))
