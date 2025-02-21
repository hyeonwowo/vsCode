def merge(a, aux, lo, mid, hi): # 해당 코드는 동일
    for k in range(lo, hi+1):
        aux[k] = a[k]
    
    i, j = lo, mid+1
    for k in range(lo, hi+1):
        if i > mid: a[k], j = aux[j], j+1            
        elif j > hi: a[k], i = aux[i], i+1            
        elif aux[i] <= aux[j]: a[k], i = aux[i], i+1
        else: a[k], j = aux[j], j+1            

    return a

# def divideNMerge(a,aux,lo,hi) 과정은 생략

# def mergeSort(a): # 기존 mergeSort(a)
#     aux = [None] * len(a)

#     divideNMerge(a, aux, 0, len(a)-1) # indexing 처리를 위한 len(a)-1
#     return a

def mergeSort(a):
    aux = [None] * len(a)

    sz = 1 # sz는 1로 시작하며 현재 병합할 서브배열의 크기를 의미
    while sz < len(a):
        for lo in range(0, len(a)-sz, sz*2): # 만약 10의 크기라면, 0-2-4-6-8 : 10까지 갈 필요가 없으니 len(a)-sz로 8까지 가도록 코드 작성
            merge(a, aux, lo, lo+sz-1, min(lo+sz+sz-1, len(a)-1)) # merge 호출 : merge(a, aux, lo, mid, hi)
        sz += sz  # 병합할 서브 배열은 두배 크기로 증가

    return a

if __name__ == "__main__":
    print(merge([1,5,2,3], [None]*4, 0, 1, 3))
    print(merge(["e","e","g","m","r","a","c","e","r","t"], [None]*10, 0, 4, 9))
    
    print(mergeSort([5,1,3,2]))
    print(mergeSort(["e","r","m","g","e","c","a","r","t","e"]))

    print(mergeSort(["m","e","r","g","e","s","o","r","t","e","x","a","m","p","l","e"]))