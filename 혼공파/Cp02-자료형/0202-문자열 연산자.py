print("hello " + "world") # " + " 사용하여 문자열 연결시 있는 그대로 연결
print("hello ","world") # " , " 사용하여 문자열 연결시 공백 하나 추가.

print("hello " + "1")
print("hello ","1")
print()

print("hello" * 3)
print(3 * "hello")
print()
print("hello\n" * 3)

# 문자열 인덱싱1
print("hello"[0])
print("hello"[1])
print("hello"[2])
print("hello"[3])
print("hello"[4])
print()

# 문자열 인덱싱2
print("hello"[-1])
print("hello"[-2])
print("hello"[-3])
print("hello"[-4])
print("hello"[-5])
print()

#  h   e   l   l   o
# [0] [1] [2] [3] [4]
# [-5][-4][-3][-2][-1] -> 역처리 생각보다 유용함. 알아두자

# 문자열 범위 연산자
print("hello"[0:5]+" [h][e][l][l][o]")
print("hello"[0:4]+" [h][e][l][l][]")
print("hello"[0:3]+" [h][e][l][][]")
print("hello"[0:2]+" [h][e][][][]")
print("hello"[0:1]+" [h][][][][]")
print()

print("hello"[1:5]+" [][e][l][l][o]")
print("hello"[1:4]+" [][e][l][l][]")
print("hello"[2:3]+" [][]][l][][]")
print()

print("hello"[0:]+ "[h][e][l][l][o]")
print("hello"[:3]+ "[h][e][l][][]")
print("hello"[3:]+ "[][][][l][o]")
print()

# 문자열과 리스트
print("hello",[0]) # hello [0] -> 이런식으로 출력되는 이유 : [0]은 리스트로 인식돼서 리스트 그 자체로 출력됨.
print("hello",[1])
print("hello",[2])
print("hello",[3])
print("hello",[4])
print()

# 문자열과 리스트
print("hello",[0,1,2,3,4,5]) # 리스트의 대괄호까지 그 자체로 출력됨.
print("hello",["a","b","c","d","e"])

# 문자열의 길이 구하기
print(len("뷁")) # len = 1
print(len("t e s t m e s s a g e")) # len = 21
print(len("t e s t m e s s a g e\n")) # len = 22
