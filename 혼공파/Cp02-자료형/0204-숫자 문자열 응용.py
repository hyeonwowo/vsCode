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

