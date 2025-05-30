import sys

def findavg(lst):
    lst.sort()
    avg = sum(lst) // len(lst)
    mid = lst[2]
    return f"{avg}\n{mid}"

if __name__ == "__main__":
    lst = [int(input()) for _ in range(5)]
    print(findavg(lst))