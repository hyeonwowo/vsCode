import sys

def phone(st):
    dial = {
        'ABC': 3,
        'DEF': 4,
        'GHI': 5,
        'JKL': 6,
        'MNO': 7,
        'PQRS': 8,
        'TUV': 9,
        'WXYZ': 10
    }

    # 알파벳 -> 숫자 변환 딕셔너리 생성
    letter_to_time = {ch: time for letters, time in dial.items() for ch in letters}

    return sum(letter_to_time[ch] for ch in st)

if __name__ == "__main__":
    st = sys.stdin.readline().strip().upper()  # 대문자 처리 보장
    print(phone(st))
