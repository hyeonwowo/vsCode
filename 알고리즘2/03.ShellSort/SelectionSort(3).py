# 역순으로 선택정렬
def selectionSort(a):    
    for i in range(len(a)-1):
        max_idx = i
        for j in range(i+1,len(a)):
            if a[max_idx] < a[j]:
                max_idx = j
        a[i],a[max_idx] = a[max_idx],a[i]
    return a
    
if __name__ == "__main__":
    print(selectionSort([5, 1, 3, 2]))
    print(selectionSort([1,3,2,4,3,5,4,6,5,7,6,8,7,9,10]))
    print(selectionSort(["b", "f", "z", "d", "i", "k", "p", "v"]))
    #selectionSort([7,2,4,1,9,0])