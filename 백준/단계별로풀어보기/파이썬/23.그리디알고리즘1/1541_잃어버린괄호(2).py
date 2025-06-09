import sys # 보다 더 많은 시간 소요(4ms) but, 간결함

def losing(expression):
    terms = expression.split('-')
    numbers = [sum(map(int, term.split('+'))) for term in terms]
    return numbers[0] - sum(numbers[1:])

if __name__ == "__main__":
    st = sys.stdin.readline().strip()
    print(losing(st))
