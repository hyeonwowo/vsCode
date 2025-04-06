lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(len(lst[0]))
print(len(lst))

reverselst = [[]*len(lst)]

for i, row in enumerate(lst):
    for j, element in enumerate(row):
        reverselst[j][i] = element
        
print(lst)
print(reverselst)