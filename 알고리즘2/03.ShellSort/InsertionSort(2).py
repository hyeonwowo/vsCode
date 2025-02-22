def insertionSort(a):    
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a
    
if __name__ == "__main__":
    print(insertionSort([5, 1, 3, 2]))
    print(insertionSort(["b", "f", "z", "d", "i", "k", "p", "v"]))
    #insertionSort([7,2,4,1,9,0])