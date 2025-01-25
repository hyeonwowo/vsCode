# 연습장

lista = ["a","b","c","d"]

# print list a with index + element

# case 1)

i=0
for element in lista:
    print(f"index : {i}, element : {element}")
    i += 1
print()

# case 2

for i in range(len(lista)):
    print(f"index : {i}, element : {lista[i]}")
print()

# case 3 : use enumerate()

print(list(enumerate(lista)))
print()

# case 4 : for & enumerate()

for index, element in enumerate(lista):
    print(f"index : {index}, element : {element}")