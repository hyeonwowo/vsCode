import sys

def phone(st):
    dictPhone = {
        'A':3,
        'B':3,
        'C':3,
        'D':4,
        'E':4,
        'F':4,
        'G':5,
        'H':5,
        'I':5,
        'J':6,
        'K':6,
        'L':6,
        'N':7,
        'M':7,
        'O':7,
        'P':8,
        'Q':8,
        'R':8,
        'S':8,
        'T':9,
        'U':9,
        'V':9,
        'W':10,
        'X':10,
        'Y':10,
        'Z':10
    }
    sum = 0
    for ch in st:
        sum += dictPhone[ch]
    return sum

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(phone(st))