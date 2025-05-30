import sys

def stacksum(n):
    lst = []
    for _ in range(n):
        inp = int(input())
        if inp == 0: lst.pop()
        else: lst.append(inp)
    return sum(lst)

if __name__ == "__main__":
    print(stacksum(int(input())))