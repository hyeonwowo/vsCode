# 리스트 요소 삭제 : pop() remove() del lst[]
lst = [11,22,33,44,55,66,77,88]

lst.pop() # 리스트의 마지막 요소 제거 및 반환
lst.pop(0) # 리스트에 첫번째 요소 제거 및 반환

lst.remove(22) # 리스트의 22 요소를 찾아서 제거
lst.remove(55) # 리스트의 55 요소를 찾아서 제거

del lst[0] # 리스트의 0번째 요소를 제거
del lst[0:3] # 리스트의 0~2번째 요소 제거
