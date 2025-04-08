import sys

def convert_to_base(B, N):  # B: 10진수 숫자, N: 진법
    resultlist = []
    bit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    B = int(B)
    N = int(N)

    if B == 0:
        return "0"

    while B > 0:
        B, rem = divmod(B, N)
        resultlist.append(bit[rem])  # 나머지를 문자열로 변환해서 추가

    resultlist.reverse()  # 가장 마지막에 구한 것이 가장 앞자리
    return ''.join(resultlist)

if __name__ == "__main__":
    B, N = sys.stdin.readline().split()
    print(convert_to_base(B, N))
