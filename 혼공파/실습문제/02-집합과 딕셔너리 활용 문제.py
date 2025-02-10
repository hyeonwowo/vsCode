# 2. 집합(Set)과 딕셔너리(Dictionary) 활용 문제
# 문제:

# 두 개의 리스트를 입력받아 공통 요소를 찾는 함수 find_common_elements(lst1, lst2)를 작성하세요. (집합 활용)
# 문자열을 입력받아, 각 문자가 몇 번 나왔는지 딕셔너리를 이용해 세는 함수 count_characters(s)를 작성하세요.

def find_common_elements(lst1, lst2):
    listA = lst1 + lst2
    unique_set = list(set(listA))
    return unique_set

def count_characters(s):
    dictA = {}
    
    for i in range(len(s)): # for char in s: - 개선된 코드
        if s[i] not in dictA: # if char not in dictA
            dictA[s[i]] = 1
        else:
            dictA[s[i]] += 1

    return dictA
    

if __name__=="__main__":
    lista = [1,2,3,4,5,6,7,8,9]
    listb = [2,4,6,8]
    listc = [1,3,5,7]

    str1 = "abcabcabcabc"
    str2 = "qweifgjfkb"
    str3 = "aaaaaaaaaaaaa"

    print(find_common_elements(lista, listb))
    print(count_characters(str1))