# f"{a} {b}" 를 활용한 출력

lst = [(1,11),(2,22),(3,33),(4,44),(5,55)]
print('\n'.join(f"{a} {b}" for a, b in lst)) # return 으로 응용해서 사용 가능
print()

for a,b in lst:
    print(a,b)