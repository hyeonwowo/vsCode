import sys

def score(records):
    scores = {
        'A+': 4.5, 'A0': 4.0,
        'B+': 3.5, 'B0': 3.0,
        'C+': 2.5, 'C0': 2.0,
        'D+': 1.5, 'D0': 1.0,
        'F' : 0.0,
    }

    total_points = total_weight = 0.0 # 한번에 초기화

    for _, credit_str, grade in records: # object -> - : 예약어 피하기 및 안쓰는 값은 _ 로 변경
        if grade == 'P':
            continue
        credit = float(credit_str)
        total_weight += credit
        total_points += credit * scores[grade]

    return total_points / total_weight if total_weight else 0.0 # 0으로 나눔 방지 처리 (예외처리 확실하게)


if __name__ == "__main__":
    records = [tuple(sys.stdin.readline().split()) for _ in range(20)]
    print(score(records))
