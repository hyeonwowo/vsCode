set1 = {1,2,3}

set1.add(1)
set1.add(4)
set1.update([1,3,4,5,6])
print(set1)

s = {1,2,3}
lista = [4,5,6]

s.add(frozenset(lista))
s.add(tuple(lista))
s.update(lista)