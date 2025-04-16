def findEnd(n):
    count = 0
    num = 666
    while True:
        if '666' in str(num):
            count += 1
            if count == n:
                return num
        num += 1

if __name__ == "__main__":
    print(findEnd(int(input())))