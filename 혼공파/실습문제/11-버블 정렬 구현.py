# 8. 정렬 알고리즘 구현
# 문제: 버블 정렬(Bubble Sort)을 직접 구현하여 리스트를 정렬하는 함수 bubble_sort(lst)를 작성하세요.

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

if __name__=="__main__":
    listA = [5,4,3,2,1]
    listB = [4,1,2,5,3]
    listC = [1,2,3,4,5]

    print(bubble_sort(listA))
    print(bubble_sort(listB))
    print(bubble_sort(listC))
