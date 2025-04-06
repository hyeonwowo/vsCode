import sys

def makearr():
    return [list(map(str, sys.stdin.readline().strip()))for _ in range(5)]

def contentArr(arr):
    maxlen = max(len(row) for row in arr)
    for i in range(5):
        while len(arr[i]) < maxlen:
            arr[i].append(' ')
    return arr
def read(arr):
    result = ''
    max_len = len(arr[0])


if __name__ == "__main__":
    