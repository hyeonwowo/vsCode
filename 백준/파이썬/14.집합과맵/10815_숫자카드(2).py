import sys

def inputdata():
    return list(map(int, sys.stdin.readline().split()))

def outputdata(resin):
    resout = list(map(int, sys.stdin.readline().split()))
    setresin = set(resin)
    result = [1 if x in setresin else 0 for x in resout]
    return ' '.join(map(str, result))

if __name__ == "__main__":
    _ = int(sys.stdin.readline())  # 첫 번째 숫자 사용 안 함
    resin = inputdata()
    _ = int(sys.stdin.readline())  # 두 번째 숫자 사용 안 함
    print(outputdata(resin))
