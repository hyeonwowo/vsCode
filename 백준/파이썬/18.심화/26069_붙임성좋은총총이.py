import sys

def chongchong(n):
    myset = set()
    myset.add("ChongChong")
    for _ in range(n):
        usera, userb = sys.stdin.readline().split()
        if usera in myset:
            myset.add(userb)
        elif userb in myset:
            myset.add(usera)
    return len(myset)

if __name__ == "__main__":
    print(chongchong(int(input())))