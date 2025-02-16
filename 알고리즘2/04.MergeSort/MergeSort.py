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
#################################
def divideNMerge(a, aux, lo, hi):
    if (hi <= lo): 
        return a
    mid = (lo + hi) // 2
    divideNMerge(a, aux, lo, mid)
    divideNMerge(a, aux, mid+1, hi)
    merge(a, aux, lo, mid, hi)
    return a

def mergeSort(a):
    aux = [None] * len(a)

    divideNMerge(a, aux, 0, len(a)-1)
    return a

if __name__ == "__main__":
    print(merge([1, 5, 2, 3], [None]*4, 0, 1, 3))
    print(merge(["e","e","g","m","r","a","c","e","r","t"], [None]*10, 0, 4, 9))
    
    print(mergeSort([5, 1, 3, 2]))
    print(mergeSort(["e","r","m","g","e","c","a","r","t","e"]))