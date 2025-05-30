def lstnum(n):
    lst = []
    i = 2
    while n != 1:
        if n % i == 0:
            lst.append(i)
            n = n // i
        elif n % i != 0:
            i += 1
    return lst

def printlst(lst):
    for element in lst:
        print(element,end = "\n")

if __name__ == "__main__":
    lst = lstnum(int(input()))
    printlst(lst)