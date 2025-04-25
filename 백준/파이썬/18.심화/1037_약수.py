import sys

def lcd(n):
    lst = list(map(int,sys.stdin.readline().split()))
    return max(lst) * min(lst)

if __name__ == "__main__":
    print(lcd(int(input())))