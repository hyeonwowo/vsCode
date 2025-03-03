# Merge a[lo ~ mid] with a[mid+1 ~ hi], using the extra space aux[]
def merge(a, aux, lo, mid, hi):
    for k in range(lo,hi+1):
        aux[k]=a[k]

    i,j = lo,mid+1
    for k in range(lo,hi+1):
        if i > mid: a[k], j = aux[j], j+1            
        elif j > hi: a[k], i = aux[i], i+1            
        elif aux[i] <= aux[j]: a[k], i = aux[i], i+1
        else: a[k], j = aux[j], j+1           
    return a

def mergeSort(a):
    aux = [None] * len(a)

    sz = 1
    while sz < len(a):
        for lo in range(0,len(a)-sz,sz*2):
            merge(a,aux,lo,lo+sz-1,min(lo+sz+sz-1, len(a)-1)) # lo, mid, hi : lo, lo+sz-1, min(lo+sz+sz-1, len(a)-1)
        sz += sz
    return a

if __name__ == "__main__":
    print(merge([1,5,2,3], [None]*4, 0, 1, 3))
    print(merge(["e","e","g","m","r","a","c","e","r","t"], [None]*10, 0, 4, 9))
    
    print(mergeSort([5,1,3,2]))
    print(mergeSort(["e","r","m","g","e","c","a","r","t","e"]))

    print(mergeSort(["m","e","r","g","e","s","o","r","t","e","x","a","m","p","l","e"]))