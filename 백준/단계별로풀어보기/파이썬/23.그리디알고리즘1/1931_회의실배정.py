import sys

def designroom(sorttime):
    result = []
    lastendtime = 0
    for element in sorttime:
        start,end = element
        if lastendtime <= start:
            result.append(element)
            lastendtime = end
    return len(result)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    time = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    sorttime = sorted(time, key=lambda x:(x[1],x[0]))
    print(designroom(sorttime))