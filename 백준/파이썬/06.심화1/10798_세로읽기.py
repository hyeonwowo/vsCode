import sys

def makeArr():
    return [list(sys.stdin.readline().strip()) for _ in range(5)]

def reverseArr(arr):
    maxlen = max(len(line) for line in arr)
    for i in range(5):
        while len(arr[i]) < maxlen:
            arr[i].append(' ')
    return arr

def readArr(arr):
    result = ''
    max_len = len(arr[0])
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] != ' ':
                result += arr[j][i]
    return result

if __name__ == "__main__":
    arr = makeArr()
    reversearr = reverseArr(arr)
    resultarr = readArr(reversearr)
    print(resultarr)
