import sys

def strRepeat(lst):
    resultST = []
    if len(lst) < 2 or not lst[1]:
        return "" # return값을 ""으로 출력해 함수내에서 처리
    for ch in lst[1]:
        resultST.append(ch * int(lst[0]))
    return "".join(resultST)

if __name__ == "__main__":
    Nst = sys.stdin.readline().strip().split()
    print(strRepeat(Nst))
