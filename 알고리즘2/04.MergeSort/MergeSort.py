def merge(a, aux, lo, mid, hi):
    for k in range(lo, hi+1):
        aux[k] = a[k]
    
    i, j = lo, mid+1
    for k in range(lo, hi+1):
        if i>mid: 
            a[k], j = aux[j], j+1            
        elif j>hi: 
            a[k], i = aux[i], i+1            
        elif aux[i] <= aux[j]: 
            a[k], i = aux[i], i+1
        else: 
            a[k], j = aux[j], j+1            

    return a

def divideNMerge(a, aux, lo, hi): # 쪼개는 과정
    if (hi <= lo): # [0 1 2 3 4 5 6 7 8 9] -> [0][1][2][3][4][5][6][7][8][9] 
        return a
    mid = (lo + hi) // 2
    divideNMerge(a, aux, lo, mid)
    divideNMerge(a, aux, mid+1, hi)
    merge(a, aux, lo, mid, hi)
    return a

def mergeSort(a):
    aux = [None] * len(a)

    divideNMerge(a, aux, 0, len(a)-1) # indexing 처리를 위한 len(a)-1
    return a

if __name__ == "__main__":
    print(merge([1, 5, 2, 3], [None]*4, 0, 1, 3))
    print(merge(["e","e","g","m","r","a","c","e","r","t"], [None]*10, 0, 4, 9))
    
    print(mergeSort([5, 1, 3, 2]))
    print(mergeSort(["e","r","m","g","e","c","a","r","t","e"]))

# 질문: 0~3의 분할과 정복이 끝날 때까지 4~7은 대기하는가?
# 네, 맞습니다!
# 재귀 함수는 스택(Stack) 구조를 따르기 때문에, 왼쪽(0~3)의 분할과 정렬이 완전히 끝난 후 오른쪽(4~7)이 실행됩니다.

# 병합정렬 재귀호출 과정 순서도. (아래로 쭉 가는 순서)
# 1. divideNMerge(0, 7)    ← 루트
#    ├── divideNMerge(0, 3) ← 왼쪽 서브트리
#    │   ├── divideNMerge(0, 1)
#    │   │   ├── divideNMerge(0, 0)  → return
#    │   │   ├── divideNMerge(1, 1)  → return
#    │   │   └── merge(0, 0, 1)  → 정렬됨 [3, 8]
#    │   ├── divideNMerge(2, 3)
#    │   │   ├── divideNMerge(2, 2)  → return
#    │   │   ├── divideNMerge(3, 3)  → return
#    │   │   └── merge(2, 2, 3)  → 정렬됨 [4, 7]
#    │   └── merge(0, 1, 3)  → 정렬됨 [3, 4, 7, 8]
#    ├── divideNMerge(4, 7) ← 오른쪽 서브트리 (왼쪽이 끝난 후 실행)
#    │   ├── divideNMerge(4, 5)
#    │   │   ├── divideNMerge(4, 4)  → return
#    │   │   ├── divideNMerge(5, 5)  → return
#    │   │   └── merge(4, 4, 5)  → 정렬됨 [2, 6]
#    │   ├── divideNMerge(6, 7)
#    │   │   ├── divideNMerge(6, 6)  → return
#    │   │   ├── divideNMerge(7, 7)  → return
#    │   │   └── merge(6, 6, 7)  → 정렬됨 [1, 5]
#    │   └── merge(4, 5, 7)  → 정렬됨 [1, 2, 5, 6]
#    └── merge(0, 3, 7)  → 최종 정렬됨 [1, 2, 3, 4, 5, 6, 7, 8]
