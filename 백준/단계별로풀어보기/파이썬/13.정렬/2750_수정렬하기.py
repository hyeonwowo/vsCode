def printlst(lst):
    for element in lst:
        print(element)

if __name__ == "__main__":
    i = int(input())
    lst = [int(input()) for _ in range(i)]
    lst.sort()
    printlst(lst)
