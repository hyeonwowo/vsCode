import sys

def strRepeat(lst):
    resultST = []
    if len(lst) < 2 or not lst[1]: # len(lst) 사용시 리스트 내부의 요소 개수 출력
        return None # return 값을 None로 설정해 main에서 처리
    for ch in lst[1]:
        resultST.append(ch * int(lst[0]))
    return "".join(resultST)

if __name__ == "__main__":
    Nst = sys.stdin.readline().strip().split()
    result = strRepeat(Nst)
    if result:
        print(result)
