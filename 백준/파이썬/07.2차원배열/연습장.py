lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(lst)
print(*lst)
reverselst = [list(row) for row in zip(*lst)]
print(reverselst)