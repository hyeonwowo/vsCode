import sys

def changeNum(N, B):  # N = ZZZZZ(수), B = 36(진법)
    dictWord = {}

    for i in range(10):
        dictWord[str(i)] = i  # '0' ~ '9' 해당부분 누락시 0~10 사이 입력시 에러 발생

    for i in range(ord('A'), ord('Z') + 1):
        dictWord[chr(i)] = i - 55  # 'A' = 65 → 65 - 55 = 10, ..., 'Z' = 90 → 35

    lst = [dictWord[ch] for ch in N]  
    reverselst = lst[::-1]

    result = 0
    for i in range(len(reverselst)):
        result += reverselst[i] * (int(B) ** i)

    return result

if __name__ == "__main__":
    N, B = sys.stdin.readline().split()
    print(changeNum(N, B))
