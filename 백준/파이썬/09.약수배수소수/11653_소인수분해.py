def lstnum(n):
    lst = []
    i = 2
    while True:
        n = n // i
        lst.append(i)
        if n % i != 0:
            i += 1

if __name__ == "__main__":
    print(lstnum(int(input())))