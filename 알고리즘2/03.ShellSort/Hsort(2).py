def shellSort(a):
    N = len(a)
    h = 1
    while h < N/3:
        h = 3*h+1
    
    while h >= 1:
        hInsertionSort(a,h)
        h = h//3
    
    return a

def hInsertionSort(a,h):
    for i in range(h,len(a)):
        key = a[i]
        j = i-h
        while j>=0 and key < a[j]:
            a[j+h] = a[j]
            j -= h
        a[j+h] = key
    return a
    
if __name__ == "__main__":
    #print(hInsertionSort(["M", "O", "L", "E", "E", "X", "A", "S", "P", "R", "T"], 3))

    a1 = ["S", "H", "E", "L", "L", "S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"]
    a2 = a1.copy()
    a3 = a1.copy()
    
    # Shell Sort with h = 13 --> 4 --> 1
    print("h-Sort with h = 13 --> 4 --> 1")
    print(hInsertionSort(a1, 13))
    print(hInsertionSort(a1, 4))
    print(hInsertionSort(a1, 1))

    # Insertion Sort
    print("Insertion Sort (i.e., Shell Sort with h = 1)")
    print(hInsertionSort(a2, 1))

    # Shell Sort with Knuth's Sequence
    #print("Shell Sort with Knuth's Sequence")
    #print(shellSort(a3))

    '''h = 1
    N = 40
    while h < N/3:        
        h = 3*h + 1
    print(h)'''
    