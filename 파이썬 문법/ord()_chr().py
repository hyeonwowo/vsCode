# ord() : 한 문자를 유니코드넘버로 변환해줌
ord('a') # 97
ord('b') # 98
ord('c') # 99
ord('d') # 100
ord('e') # 101


# chr() : 한 숫자를 문자로 변환해줌
chr(97) # 'a'
chr(98) # 'b'
chr(99) # 'c'
chr(100) # 'd'
chr(101) # 'e'


# 예제1) 알파벳 출력하기
for i in range(ord('a'),ord('z')+1):
    print(chr(i),end=' ')