import random

def shuffleSort(a):
    r = [random.random() for _ in range(len(a))]
    return [i for i,_ in sorted(zip(a,r), key=lambda x:x[1])]

def knuthShuffle(a):
    for i in range(1,len(a)):
        j = random.randint(0,i)
        a[i],a[j] = a[j],a[i]
    return a

if __name__ == "__main__":
    lista = [1,2,3,4,5]
    listb = ["b", "f", "z", "d", "i", "k", "p", "v"]
    listc = [11,22,33,44,55]
    listd = ["b", "f", "z", "d", "i", "k", "p", "v"]
    print(shuffleSort(lista))
    print(shuffleSort(listb))
    print(knuthShuffle(listc))
    print(knuthShuffle(listd))
