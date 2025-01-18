# 문자열 format() 함수

num = int(input("type num data >> "))

stringA = "{}".format(num)
print("your typed data is :", stringA)

stringB = "your typed data is : {}".format(num)
print(stringB)

# 문자열 format() 함수(2)

stringA = "{} {} {} {} {}".format(10,20,30,40,50)
print(stringA, type(stringA))

# 문자열 format() 함수(3)
outputa = "{:d}".format(52)
outputb = "{:5d}".format(52)
outputc = "{:10d}".format(52)
outputd = "{:05d}".format(52)
outpute = "{:05d}".format(-52)

print(outputa)
print(outputb)
print(outputc)
print(outputd)
print(outpute)

outputf = "{:+d}".format(52)
outputg = "{:+d}".format(-52)
outputh = "{: d}".format(52)
outputi = "{: d}".format(-52)

print(outputf)
print(outputg)
print(outputh)
print(outputi)

outputh = "{:+5d}".format(52)
outputi = "{:+5d}".format(-52)
outputj = "{:=+5d}".format(52)
outputk = "{:=+5d}".format(-52)
outputl = "{:+05d}".format(52)
outputm = "{:+05d}".format(-52)

print(outputh)
print(outputi)
print(outputj)
print(outputk)
print(outputl)
print(outputm)
print()

output_a = "{:f}".format(3.141592)
output_b = "{:15f}".format(3.141592) # 15칸 만들기
output_c = "{:+15f}".format(3.141592) # 15칸에 부호 추가
output_d = "{:+015}".format(3.141592) # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print()

output_e = "{:15.3f}".format(3.141592) # 소수점 아래 세자리 - 3.141
output_f = "{:15.2f}".format(3.141592) # 소수점 아래 두자리 - 3.14
output_g = "{:15.1f}".format(3.141592) # 소수잠 아래 한자리 - 3.1

print(output_e)
print(output_f)
print(output_g)
print()

outputA = 3.0
outputB = "{:g}".format(outputA) # .0 제거
outputC = 3.14000 # 얘는 굳이 "{:g}" 안써줘도, 0을 쳐내줌.
outputD = "{:g}".format(outputC)


print(outputA) # 3.0
print(outputB) # 3
print(outputC) # 3.14
print(outputD) # 3.14
print()


