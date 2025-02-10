# 5. 세트(Set) 활용
# 문제: 두 개의 리스트를 입력받아, 두 리스트의 교집합, 합집합, 차집합을 각각 반환하는 함수 set_operations(lst1, lst2)를 작성하세요.

def set_operations(lst1, lst2):
    set1, set2 = set(lst1),set(lst2)

    res1 = set1 & set2
    res2 = set1 | set2
    res3 = set1 - set2

    return res1,res2,res3

if __name__=="__main__":
    lst1 = [1,2,3,4,5,1,2,3,4,5]
    lst2 = [1,3,5]

    res1,res2,res3 = set_operations(lst1,lst2)
    
    print("교집합 : ",res1)
    print("합집합 : ",res2)
    print("차집합 : ",res3)

