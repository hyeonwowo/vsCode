import sys

def divideSum(k):
    # 1부터 k까지 모든 수를 생성자 후보로 검사 (생성자는 자기 자신보다 클 수 없음)
    for n in range(1, k + 1):
        result = n + divide(n)
        if k == result:
            return n
    return 0

def divide(n):
    return sum(map(int, str(n)))

if __name__ == "__main__":
    print(divideSum(int(input())))
