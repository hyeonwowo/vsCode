def mergeSort(a):
    lo, mid = 0, len(a)//2 + 1
    result = []

    i = lo
    j = mid

    while True:
        if a[i] <= a[j]:
            result.append(a[i])
            i += 1
        elif a[i] > a[j]:
            result.append(a[j])
            j += 1
        elif i < mid:
            result.append(a[j])
            j += 1
        elif j < len(a):
            result.append(a[i])
            i += 1
        else:
            break


    return result

if __name__ == "__main__":
    lista = [4,6,2,7,8,9,0,1,2,4,3,5,6]
    print(lista)
    print(mergeSort(lista))