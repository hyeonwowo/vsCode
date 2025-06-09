# 특정 조건수와 max()의 사용
lst = [10,50,100,500,1000]
coin = 300
maxcoin = max([element for element in lst if element < coin])
print(maxcoin)


print()
# 문자열 공식 계산
st = "50+40"
if '+' in st:
    a, b = map(int, st.split('+'))
    print(a+b)
elif '-' in st:
    a, b = map(int, st.split('-'))
    print(a-b)