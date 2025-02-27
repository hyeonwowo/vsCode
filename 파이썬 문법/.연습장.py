data = [(1,111),(2,222),(3,333)]

lista = [p[0] for p in data]
print(lista)

listaa = [p[1] for p in data]

listb = [i for i,_ in data]
listc = [i for _,i in data]

print(lista)
print(listaa)
print(listb)
print(listc)
