# f-문자열

a = "{}".format(10)
b = f'{10}'

print(a)
print(b)

print(f'3 + 7 = {3+7}') # f"string {숫자 표현식}" -  이와 같은 방법을 많이 사용함
print("3 + 7 = {}".format(3+7)) # "{}".format() - 방식이 더 유용할 때가 있음.

    # 1) 문자열 내용이 너무 많을 때
name = "구름"
age = 7

print('test message test message{} test message test messsage{} test message test message test message'.format(name,age))
print()

    # 2) 데이터를 리스트에 담아 사용할 때
listA = ["shin",25, 181.3, "comp"]
print(f"""name : {listA[0]}, age : {listA[1]}, height : {listA[2]}, major : {list[3]}""") # 불편한 방법 1
print('name : {}, age : {}, height : {}, major : {}'.format(listA[0],listA[1],listA[2],listA[3])) # 불편한 방법 2
print('name : {}, age : {}, height : {}, major : {}'.format(*listA)) # *listA 를 통해 간편하게 수행 가능
print()
