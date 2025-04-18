import sys

def companyLog(n):
    log = set()
    for _ in range(n):
        name, status = sys.stdin.readline().split()
        if status == "enter":
            log.add(name)
        else:
            log.discard(name)  # 안전하게 제거
    return '\n'.join(sorted(log, reverse=True))

if __name__ == "__main__":
    print(companyLog(int(sys.stdin.readline())))
