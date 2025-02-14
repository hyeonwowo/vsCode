# Merge a[lo ~ mid] with a[mid+1 ~ hi], using the extra space aux[]
def merge(a, aux, lo, mid, hi):
    return a

# Halve a[lo ~ hi], sort each of the halves, and merge them, using the extra space aux[]
def divideNMerge(a, aux, lo, hi):
    return a

def mergeSort(a):
    return a

if __name__ == "__main__":
    print(merge([1, 5, 2, 3], [None]*4, 0, 1, 3))
    print(merge(["e","e","g","m","r","a","c","e","r","t"], [None]*10, 0, 4, 9))
    
    print(mergeSort([5, 1, 3, 2]))
    print(mergeSort(["e","r","m","g","e","c","a","r","t","e"]))