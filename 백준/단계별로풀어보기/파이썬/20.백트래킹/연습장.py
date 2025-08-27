lst = [2,0,0,2,2,0,4]
res = []

# 일단은 0 제거
newlst = []
for element in lst:
    if element != 0:
        newlst.append(element)
print(newlst)

lst = [2,2,4,2,4] # 좌측방향으로 합치기 -> [4,4,2,4]

i = 0
while i < len(lst):
    if i+1 < len(lst) and lst[i] == lst[i+1]:
        res.append(lst[i]+lst[i+1])
        i += 2
    else:
        res.append(lst[i])
        i += 1
print(res)