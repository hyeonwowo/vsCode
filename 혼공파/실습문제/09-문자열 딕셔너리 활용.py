# . 문자열 딕셔너리 활용
# 문제: 문자열을 입력받아 각 단어의 등장 횟수를 딕셔너리로 저장하여 반환하는 함수 word_count(s)를 작성하세요.

def word_count(s):
    dictA = {}

    for char in s:
        if char not in dictA:
            dictA[char] = 1
        else:
            dictA[char] += 1

    return dictA

if __name__=="__main__":
    str1 = "ababdsbfasbffuacuvaiosfkleqwfj ioajvklxzj vklasdjfklajwavnmxz,cnv qwilof aqwjuf laksdfj"

    dictA = word_count(str1)

    print(dictA) # 딕셔너리 그대로 출력
    print()

    for element in dictA: # 가독성 좋게 분리해서 출력
        print(element,":",dictA[element])